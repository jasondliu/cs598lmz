import signal
# Test signal.setitimer
#
# This test is not very good.  It just checks that the timer fires
# and that it doesn't fire too early.  It doesn't check that it fires
# at the right time.

def handler(signum, frame):
    print("Timer fired")
    raise SystemExit

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

# We expect the timer to fire (and the program to exit) within
# 0.2 seconds.
time.sleep(0.2)

# If we get here, the timer didn't fire.
print("Timer didn't fire")
raise SystemExit
