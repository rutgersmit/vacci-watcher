import datetime

def log_msg(msg):
    now = datetime.datetime.now()
    msg = '{} - {}'.format(now.strftime('%d/%m/%Y  %H:%M:%S'), msg)
    
    f = open('log/log-{}.txt'.format(now.strftime('%Y-%m-%d')), "a")
    f.writelines(msg + '\n')
    f.close()

    print(msg, flush=True)