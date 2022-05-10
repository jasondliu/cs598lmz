import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.25, 0.25)

def handler(signum, frame):
    print "signum =", signum
    print "frame =", frame
    print "Handling timer..."

signal.signal(signal.SIGALRM, handler)

# Wait for the timer to expire
time.sleep(1)

# Disable the timer
signal.setitimer(signal.ITIMER_REAL, 0, 0)

# Wait for the timer to expire
time.sleep(5)
