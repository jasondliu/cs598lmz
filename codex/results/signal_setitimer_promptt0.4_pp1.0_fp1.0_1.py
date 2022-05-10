import signal
# Test signal.setitimer()
#
# This test is not exhaustive.  It only tests the basic functionality.

# Test the basic functionality of setitimer()

def handler(signum, frame):
    print("handler")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(0.2)
signal.setitimer(signal.ITIMER_REAL, 0)

# Test that the timer fires at least once

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(0.2)
signal.setitimer(signal.ITIMER_REAL, 0)

# Test that the timer fires at least twice

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(0.3)
