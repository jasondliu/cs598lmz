import signal
# Test signal.setitimer() and os.getitimer().


signal.setitimer(signal.ITIMER_REAL, 0.1, 0)
# Set an interval timer, nonzero.

signal.setitimer(signal.ITIMER_VIRTUAL, 0.0001, 0.01)
# Set it again with a different kind.

remaining = os.getitimer(signal.ITIMER_VIRTUAL)
if remaining != 0.0001:
    print("remaining %.5f != .0001" % remaining)

signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)
# Stop the timer.

remaining = os.getitimer(signal.ITIMER_VIRTUAL)
if remaining != 0:
    print("remaining %.5f != 0" % remaining)
