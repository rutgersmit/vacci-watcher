if not selenium_host:
    print('⚠ No Selenium hostname (SELENIUM_REMOTE_HOSTNAME) specified in the environment variables. Falling back to localhost.')
    selenium_host = 'localhost'
else:
    print('Selenium host: {}'.format(selenium_host))

if not token:
    print('⚠ No Telegram token (TELEGRAM_TOKEN) specified in the environment variables. No alerts will be sent.')
else:
    print('Telegram token: {}'.format(token))

if not chatid:
    print('⚠ No Telegram chat id (TELEGRAM_CHATID) specified in the environment variables. No alerts will be sent.')
else:
    print('Telegram chatid: {}'.format(chatid))

if not interval:
    print('No interval (INTERVAL) specified in the environment variables. Defaulting to 60 seconds.')
    interval = 60
else:
    print('Check interval: {}'.format(interval))


if not interval_standby:
    print('No interval during standby (INTERVAL_STANDBY) specified in the environment variables. Defaulting to 300 seconds.')
    interval = 300
else:
    print('Standby interval: {}'.format(token))