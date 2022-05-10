import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "Got signal", signum
    if signum == signal.SIGALRM:
        print "SIGALRM"
    elif signum == signal.SIGVTALRM:
        print "SIGVTALRM"
    else:
        print "Other signal"

signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGVTALRM, handler)

# Set the timer for 5 seconds
signal.setitimer(signal.ITIMER_REAL, 5, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 5, 0)

# Wait for the timer to expire
while True:
    time.sleep(1)
