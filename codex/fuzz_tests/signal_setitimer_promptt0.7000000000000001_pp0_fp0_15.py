import signal
# Test signal.setitimer()
# Demonstrate that alarm() does not interrupt a system call
# and is instead received upon completion of the system call
def handler(signum, frame):
    print "Signal handler called with signal", signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
print open("/tmp/does/not/exist", "r")
