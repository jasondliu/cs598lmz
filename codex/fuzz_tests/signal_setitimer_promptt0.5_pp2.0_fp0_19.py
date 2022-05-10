import signal
# Test signal.setitimer()

import signal

def handler(signum, frame):
    print "got signal", signum

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0)

print "Waiting for SIGALRM"
signal.pause()
print "Done"
