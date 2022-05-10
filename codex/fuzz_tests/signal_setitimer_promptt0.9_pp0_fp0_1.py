import signal
# Test signal.setitimer
# This example is from http://www.cyberciti.biz/faq/python-setitimer-example-to-handle-unwanted-child-process/

def time_expired(signum, frame):
	print "Time's up!"
	raise SystemExit
	
print "Setting up signal handler..."
signal.signal(signal.SIGALRM, time_expi
