import signal
# Test signal.setitimer
def handler(signum=0,frame=None):
	print("Signal handler called with signal",signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM,handler)
signal.setitimer(signal.ITIMER_REAL,5)

# This open-coded sleep() call will be interrupted
while True:
	pass
