import os
import datetime

import log

now = datetime.datetime.now()
selenium_host = os.environ['REMOTE_SELENIUM_HOSTNAME']
token = os.environ['TELEGRAM_TOKEN']
chatid = os.environ['TELEGRAM_CHATID']
city = os.environ['VACCINATION_CITY']
interval = os.environ['INTERVAL']

if not interval.isnumeric():
    interval = None
else:
    interval = int(interval)


if not selenium_host:
    log.log_msg('⚠ No Selenium hostname (SELENIUM_REMOTE_HOSTNAME) specified in the environment variables. Falling back to localhost.')
    selenium_host = 'localhost'
else:
    log.log_msg('Selenium host: {}'.format(selenium_host))

if not token:
    log.log_msg('⚠ No Telegram token (TELEGRAM_TOKEN) specified in the environment variables. No alerts will be sent.')
else:
    log.log_msg('Telegram token: {}'.format(token))

if not chatid:
    log.log_msg('⚠ No Telegram chat id (TELEGRAM_CHATID) specified in the environment variables. No alerts will be sent.')
else:
    log.log_msg('Telegram chatid: {}'.format(chatid))

if not interval:
    log.log_msg('No interval (INTERVAL) specified in the environment variables. Defaulting to 60 seconds.')
    interval = 60
else:
    log.log_msg('Check interval: {}'.format(interval))