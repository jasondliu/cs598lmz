import signal
# Test signal.setitimer()
#
# This test is a bit tricky.  We need to set an alarm for a few seconds
# in the future, and then wait for it to go off.  We can't just use
# time.sleep() to wait, because that will be interrupted by the alarm.
# Instead, we use select.select() to wait for the alarm.

# Set an alarm for 5 seconds in the future
signal.setitimer(signal.ITIMER_REAL, 5)

# Wait for the alarm
r, w, x = select.select([], [], [], 10)
if r or w or x:
    raise TestFailed, "select() returned %s, %s, %s" % (r, w, x)

# Make sure the alarm went off
if signal.getitimer(signal.ITIMER_REAL) != (0.0, 0.0):
    raise TestFailed, "getitimer() != (0.0, 0.0)"

# Make sure the alarm only went off once
signal.setitimer(signal.ITIMER_
