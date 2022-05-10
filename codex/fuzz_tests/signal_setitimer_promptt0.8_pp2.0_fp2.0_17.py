import signal
# Test signal.setitimer() in Python 3.0 using the new SIGALRM signal.
# Default signal.signal() handler does not call the previous signal handler,
# so install one to bump the counter for us.  For example:
#
# >>> import signal, time
# >>> def bump(sig, frame):
# ...     global count
# ...     count += 1
# ...     print(count, "bump() called")
# ...     signal.setitimer(signal.ITIMER_REAL, 0.5)
# ...
# >>> signal.signal(signal.SIGALRM, bump)
# >>> signal.setitimer(signal.ITIMER_REAL, 0.5)
# >>> time.sleep(2)
# 1 bump() called
# 2 bump() called
# 3 bump() called
# >>> signal.setitimer(signal.ITIMER_REAL, 0.0)
# >>> count
# 3
#
# If Python 3.0 fails to call bump(), the test will exit after about 4.0 seconds.
# That gives the signal handler time to be installed and
