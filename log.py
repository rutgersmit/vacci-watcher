import datetime

def log_msg(msg):
    now = datetime.datetime.now()
    print('{} - {}'.format(now.strftime('%d/%m/%Y  %H:%M:%S'), msg))
