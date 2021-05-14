import os

token = os.environ['TELEGRAM_TOKEN']
chatid = os.environ['TELEGRAM_CHATID']
city = os.environ['VACCINATION_CITY']

interval = os.environ['INTERVAL']
if not interval.isnumeric():
    interval = None
else:
    interval = int(interval)

interval_standby = int(os.environ['INTERVAL_STANDBY'])
if not interval_standby.isnumeric():
    interval_standby = None
else:
    interval_standby = int(interval_standby)
