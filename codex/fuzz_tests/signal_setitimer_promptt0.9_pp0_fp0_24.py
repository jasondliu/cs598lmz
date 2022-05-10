import signal
# Test signal.setitimer() and signal.getitimer()

# Test the timer expiration signal.
def handler(signum, frame):
    print("handler executed")
    # Do something...
    # Schedule this handler again.
    signal.setitimer(signal.ITIMER_REAL, 0.2)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
print("Starting")
time.sleep(1)
print("Exiting")
