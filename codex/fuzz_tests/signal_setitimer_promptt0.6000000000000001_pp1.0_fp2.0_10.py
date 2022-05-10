import signal
# Test signal.setitimer()

# Note that this test does not test if the timer works,
# it only tests if the call to setitimer() works.

def handler(signum, frame):
    print("Got signal", signum)

signal.setitimer(signal.ITIMER_REAL, 1)
try:
    signal.signal(signal.SIGALRM, handler)
    while True:
        pass
except KeyboardInterrupt:
    pass
finally:
    signal.setitimer(signal.ITIMER_REAL, 0)
