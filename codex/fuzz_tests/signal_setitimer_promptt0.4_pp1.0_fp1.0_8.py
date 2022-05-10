import signal
# Test signal.setitimer and signal.setitimer_ms

# This test is only valid on systems that support ITIMER_REAL.
try:
    signal.setitimer(signal.ITIMER_REAL, 0)
except ValueError:
    raise unittest.SkipTest("ITIMER_REAL not supported")

# Test the basic functionality
def handler(signum, frame):
    pass

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(0.2)
signal.setitimer(signal.ITIMER_REAL, 0)

# Test that the timer fires only once
def handler2(signum, frame):
    raise AssertionError("timer fired too many times")

signal.signal(signal.SIGALRM, handler2)
signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(0.2)
signal.setitimer(signal
