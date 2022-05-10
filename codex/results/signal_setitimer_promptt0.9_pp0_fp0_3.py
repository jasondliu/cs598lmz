import signal
# Test signal.setitimer
def timeout_handler(signum, frame):
	print 'Received signal: %s' % signum
	print 'Frame: %s' % frame
	signal.setitimer(signal.ITIMER_REAL, 1.0)

signal.signal(signal.SIGALRM, timeout_handler)
signal.setitimer(signal.ITIMER_REAL, 1.0)
while True:
	print 'Hello world'
	time.sleep(1)
