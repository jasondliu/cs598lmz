import signal
# Test signal.setitimer()

def handler (signum, frame):
    print "handler", signum, frame

def target ():
    print "target"

signal.setitimer (signal.ITIMER_REAL, 0.1, 0)
signal.signal (signal.SIGALRM, handler)
target ()
