import signal
# Test signal.setitimer
# This is used by the test_keyboardinterrupt test to make sure
# KeyboardInterrupt exceptions are raised at regular intervals.
#
# Use it like this, in a Python subprocess:
#
#     signal.signal(signal.SIGALRM, handler)
#     signal.setitimer(signal.ITIMER_REAL, interval, interval)
#     while True:
#         try:
#             # Do some useful work here
#         except KeyboardInterrupt:
#             # Record that we got a KeyboardInterrupt
#     signal.setitimer(signal.ITIMER_REAL, 0, 0)
#     # Report results
#
# The handler may be a Python function or SIG_IGN or SIG_DFL.
#
# Note: using SIGALRM is a bit unclean, since signal.alarm() and alarm()
# may also be in use.  However, it should be OK: both setitimer() and alarm()
# use the same signal, and we block signals in the main thread while
# the handler is running, so we should never run into a
