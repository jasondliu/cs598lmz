import signal
# Test signal.setitimer()

def setitimer_handler(signum, frame):
    print "setitimer_handler() called"
    raise SystemExit

signal.signal(signal.SIGALRM, setitimer_handler)

print "starting"
signal.setitimer(signal.ITIMER_REAL, 2.0, 2.0)

# Busy loop
i = 0
while i < 10000000:
    i += 1

print "ending"
