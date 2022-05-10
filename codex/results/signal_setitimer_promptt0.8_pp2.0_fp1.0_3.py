import signal
# Test signal.setitimer()

def handler(signum, frame):
    print('Signal handler called with signal', signum)

# Register signal handler
signal.signal(signal.SIGVTALRM, handler)

## previous wassignal.ITIMER_VIRTUAL
# Initially, we just want the timer to fire once, 3 seconds from now
signal.setitimer(signal.ITIMER_VIRTUAL, 3, 0)
while True:
    print('Hi!')
    time.sleep(1)  # Delay for 1 second

# This is a test

# This is a test again
