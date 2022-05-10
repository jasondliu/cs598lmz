import signal
# Test signal.setitimer and time.sleep.
# This is used by test_threaded_import to see whether the current
# thread is interrupted by a signal (yes, on systems that support
# threaded imports).
#
# XXX The output of this test is misleading: it prints "OK" even if
# threads don't work (on OpenBSD 3.0, at least).
def alarm_received(*args):
    print("OK")
    os._exit(0)

def set_and_sleep():
    signal.signal(signal.SIGALRM, alarm_received)
    # On Linux, we can't use SIGALRM, since the alarm interrupt is
    # delivered on a separate thread.  time.sleep doesn't
    # interrupt the sleep.  SIGVTALRM is uninterruptible and thus
    # useless as well.
    # signum = signal.SIGALRM
    signum = signal.SIGUSR1
    signal.setitimer(signal.ITIMER_REAL, 1.0)
