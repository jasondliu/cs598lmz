import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("got signal", signum)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

# Wait for the timer to expire
while True:
    pass
