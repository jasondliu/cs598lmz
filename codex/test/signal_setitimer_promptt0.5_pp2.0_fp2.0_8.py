import signal
# Test signal.setitimer()
# http://docs.python.org/library/signal.html

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException()

def test_timeout():
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(2)
