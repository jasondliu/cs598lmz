import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        sys.exit(0)

signal.signal(signal.SIGALRM, handler)
print "Installing a timer for 10 seconds"
signal.setitimer(signal.ITIMER_REAL, delays.pop())

def testsig():
    print 'nice'

class Context(object):
    def __init__(self, *args):
        print 'init', args

    def __enter__(self):
        print "entering with context"
        return self
    def __exit__(self, ex_type, ex_value, traceback):
        testsig()
        print "test signal", ex_type, ex_value, traceback
        return True

with Context(1):
    print "loop started"
    while True:
        pass
