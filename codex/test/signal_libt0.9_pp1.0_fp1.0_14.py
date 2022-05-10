import signal
signal.signal(signal.SIGINT, signal_handler)

SERVICE = 'MIXCLOUD_USER'

u = login(SERVICE)
u.select('user')
m = Mixcloud()

