import os

selenium_host = os.environ['REMOTE_SELENIUM_HOSTNAME']
token = os.environ['TELEGRAM_TOKEN']
chatid = os.environ['TELEGRAM_CHATID']
city = os.environ['VACCINATION_CITY']

interval = os.environ['INTERVAL']
if not interval.isnumeric():
    interval = None
else:
    interval = int(interval)

interval_standby = os.environ['INTERVAL_STANDBY']
if not interval_standby.isnumeric():
    interval_standby = None
else:
    interval_standby = int(interval_standby)


if not selenium_host:
    print('⚠ No Selenium hostname (SELENIUM_REMOTE_HOSTNAME) specified in the environment variables. Falling back to localhost.')
    selenium_host = 'localhost'

if not token:
    print('⚠ No Telegram token (TELEGRAM_TOKEN) specified in the environment variables. No alerts will be sent.')

if not chatid:
    print('⚠ No Telegram chat id (TELEGRAM_CHATID) specified in the environment variables. No alerts will be sent.')   

if not interval:
    print('No interval (INTERVAL) specified in the environment variables. Defaulting to 60 seconds.')   
    interval = 60

if not interval_standby:
    print('No interval during standby (INTERVAL_STANDBY) specified in the environment variables. Defaulting to 300 seconds.')   
    interval = 300


