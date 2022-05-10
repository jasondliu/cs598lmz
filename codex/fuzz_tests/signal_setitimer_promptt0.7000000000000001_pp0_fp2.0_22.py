import signal
# Test signal.setitimer()
# Example from PEP 475

import errno

def signal_handler(signum, frame):
    print('Alarm')
    raise OSError("getcwd: '%s'" % path)

def test_setitimer():
    signal.signal(signal.SIGALRM, signal_handler)

    signal.setitimer(signal.ITIMER_REAL, 0.1)
    try:
        os.getcwd()
    except OSError as e:
        print(e.errno)
        assert e.errno == errno.EINTR
    else:
        raise AssertionError('OSError not raised')

    signal.setitimer(signal.ITIMER_REAL, 0)
    # This should not raise OSError
    os.getcwd()
