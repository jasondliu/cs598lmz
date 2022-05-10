import signal
# Test signal.setitimer()
# This is a very simple test that does not check the exact timing.

signal.setitimer(signal.ITIMER_REAL, 0.25, 0.25)

def handler(signum, frame):
	global counter
	counter += 1
	if counter == 3:
		signal.setitimer(signal.ITIMER_REAL, 0.0, 0.0)
		raise KeyboardInterrupt

counter = 0
signal.signal(signal.SIGALRM, handler)
while 1:
	pass
