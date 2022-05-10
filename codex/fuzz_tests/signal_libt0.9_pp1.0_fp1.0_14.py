import signal
signal.signal(signal.SIGINT, signal_handler)

SERVICE = 'MIXCLOUD_USER'

u = login(SERVICE)
u.select('user')
m = Mixcloud()

while True:
    try:
        user_id = sys.stdin.readline()
        
        if not user_id:
            break

        user_id = user_id.strip()

        data = {'id':user_id, '_root': 'cloudcasts'}
        m.call('/ladrope', 'user', data, callback_comment)
    except Exception, e:
        print e

    print '========================================================='
