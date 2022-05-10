import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 0.2, 0.2)
time.sleep(0.5)
if (times_called != 2):
    fail("After sleep(0.5 s), timer fired %d times, expected 2" % times_called)
times_called = 0
signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)
time.sleep(0.5)
if (times_called != 0):
    fail("After sleep(0.5 s), timer fired %d times, expected 0" % times_called)
