import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
def handler(signum, frame):
	signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
	print('Timer is off...')
signal.signal(signal.SIGALRM, handler)
while True:
	pass
