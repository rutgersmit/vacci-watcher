import log
import config
import requests
import datetime
import threading
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# we need some time to be sure the selenium container is running
time.sleep(5)

options = Options()
options.headless = True
options.add_argument("--log-level=3")

driver = None


def init_driver():
    # initialize the driver that connects to the selenium container
    log.log_msg('Init driver')

    global driver
    driver = webdriver.Remote(
               options=options,
               command_executor='http://{}:4444/wd/hub'.format(config.selenium_host),
               desired_capabilities=DesiredCapabilities.CHROME)

def send_message(message):
    url_req = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(config.token, config.chatid, message)
    requests.get(url_req)


def check():
    # check if we really need to check. The vaccionations are only expected at the last part of the workday
    now = datetime.datetime.now()
    if now.hour < 15 or now.hour > 20:
        log.log_msg('Buiten het vaccinatie window.')

    else:
        try:
            if driver is None:
                init_driver()

            # open the site
            driver.get('https://www.prullenbakvaccin.nl/')

            # find the serch box
            inputElement = driver.find_element_by_name('location')

            # enter the city and hit enter
            inputElement.send_keys(config.city)
            inputElement.send_keys(Keys.ENTER)

            locations = driver.find_elements_by_xpath('//h5[@class="card-title"]')

            for location in locations:
                if 'vaccins beschikbaar' in location.text:
                    p = location.find_element_by_xpath('..').find_elements_by_tag_name('h1')
                    msg = '⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠\n💉Er is een vaccin beschikbaar 💉\n⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠'
                    if len(p)>1:
                        msg = msg + '\n' + p[1].text
                    send_message(msg + '\nhttps://www.prullenbakvaccin.nl/')


        except Exception as e:
            log.log_msg('Error')
            log.log_msg(e)
            
            if 'invalid session id' in e:
                init_driver()


    log.log_msg('Volgende check om {}'.format((now+datetime.timedelta(0,config.interval)).strftime('%d/%m/%Y %H:%M:%S')))


if __name__ == "__main__":
    while True:
        check()
        time.sleep(config.interval)
