import signal
# Test signal.setitimer
# Function to call when timer expires
def handler(signum, frame):
	print "Timer expired"

# Install signal handler
signal.signal(signal.SIGALRM, handler)

# Set timer for 1 second
signal.setitimer(signal.ITIMER_REAL, 1)

# Wait for timer to expire
signum = 0
while True:
	if signum == signal.SIGALRM:
		break
	signum = signal.pause()

# Remove signal handler
signal.signal(signal.SIGALRM, signal.SIG_DFL)
