import signal
# Test signal.setitimer() with alarm()
#
# This test is for a bug reported by Jiri Horky, where
# setitimer() with ITIMER_REAL and a non-zero value
# would not cause the alarm() handler to be called.
#
# The test is a bit of a hack: it sets the alarm()
# to go off in the near future, and then sets the
# timer to expire in the near future, and then
# waits for the timer to expire.  The alarm() handler
# should be called, but the test would hang if the
# bug is present.

