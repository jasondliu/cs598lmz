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
    try:
        print 'Waiting for 3 seconds...'
        time.sleep(3)
    except TimeoutException:
        print '3 seconds passed.'


# Test signal.setitimer()
# http://docs.python.org/library/signal.html
class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException()

def test_timeout():
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(2)
    try:
        print 'Waiting for 3 seconds...'
        time.sleep(3)
    except TimeoutException:
        print '3 seconds passed.'

# Test signal.
