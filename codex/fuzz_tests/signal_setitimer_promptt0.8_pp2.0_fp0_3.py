import signal
# Test signal.setitimer()
#
"""
Cancel the timer then start it again, continue when the timer 
starts to expire.

The first timer is a virtual timer that is not reset when the 
process is blocked.   

The second timer is a real timer.
"""

def print_msg(type):
	print("caught " + type + " signal")

def sig_handler(signo, sigobj):
	print("sig_handler() called")
	print("signo = " + str(signo))
	print("sigobj = " + str(sigobj))

def main():
	# Set up a signal handler
	signal.signal(signal.SIGALRM, sig_handler)

	# Set up a virtual timer
	signal.setitimer(signal.ITIMER_VIRTUAL, 2, 1.5)
	
	# Set up a real timer
	signal.setitimer(signal.ITIMER_REAL, 4, 2.5)

	# Process in an infinite loop till a signal is received
	while 1:
