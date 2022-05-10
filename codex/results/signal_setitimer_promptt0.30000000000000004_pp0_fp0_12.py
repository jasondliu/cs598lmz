import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Received signal", signum)

signal.signal(signal.SIGALRM, handler)

# Set an alarm for 1 second
signal.setitimer(signal.ITIMER_REAL, 1)

# Do some work
time.sleep(5)
