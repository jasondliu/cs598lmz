import signal
# Test signal.setitimer
import _testcapi


def handler_sig_bogus(*args):
    print("handler_sig_bogus", args)
    raise _testcapi.TestFailed("wrong signal")


def handler(*args):
    print("handler", args)
    try:
        signal.setitimer(signal.ITIMER_REAL, 0.123)
        raise _testcapi.TestFailed("shouldn't be able to set timer inside handler")
    except OSError as ex:
        if ex.errno != errno.EINVAL:
            raise _testcapi.TestFailed("didn't get expected exception")
    # Clear the alarm
    signal.setitimer(signal.ITIMER_REAL, 0)
    # Check that alarm() works inside the handler.  Without
    # using a small value, this test can last forever.
    signal.alarm(1)
    time.sleep(1)
    signal.alarm(0)

def handler_raise(*args):
    raise KeyboardInterrupt

def handler
