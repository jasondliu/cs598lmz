import signal
# Test signal.setitimer(mode, interval, interval)
#   mode: ITIMER_REAL, ITIMER_VIRTUAL, ITIMER_PROF
#   interval: integer in sec, 0.0 to disable
#   interval: integer in usec, 0 to disable

# Note: this test relies on the fact that the timer is set to 0.5 seconds
# and that it is set with ITIMER_REAL.
# If this is not the case, the test will fail.

# The test itself doesn't start a timer, so the timer_handler won't
# be called.

timer_handler_called = False

def timer_handler(sig, frame):
    global timer_handler_called
    timer_handler_called = True

signal.signal(signal.SIGALRM, timer_handler)

# Note: for now, the test only checks that the call doesn't crash
# and that the timer handler isn't called.

# ITIMER_REAL
signal.setitimer(signal.ITIMER_REAL, 0.0, 0)
sign
