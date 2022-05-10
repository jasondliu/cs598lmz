import signal
# Test signal.setitimer
# This test is Linux-specific, so skip it on other platforms.
if sys.platform.startswith('linux'):
    import signal
    import time
    import os

    def alarm_handler(signum, frame):
        print('Got SIGALRM')
        raise SystemExit

    signal.signal(signal.SIGALRM, alarm_handler)

    # Test signal.setitimer
    signal.setitimer(signal.ITIMER_REAL, 0.1)
    time.sleep(0.2)

    # Test signal.setitimer with negative time
    signal.setitimer(signal.ITIMER_REAL, -1)
    time.sleep(0.2)

    # Test signal.setitimer overflow
    # The it_value member is a float representing the input to setitimer
    # in seconds.  The it_value member will normally be rounded up to
    # the system clock granularity, and will not be less than the
    # resolution of the system clock.  (POSIX.1-2001, 4.7.1)
