import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Got signal', signum

signal.signal(signal.SIGALRM, handler)

def test_itimer_once():
    signal.setitimer(signal.ITIMER_REAL, 0.1)
    time.sleep(0.2)
    print "OK"

def test_itimer_repeated():
    signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
    time.sleep(0.4)
    print "OK"

def test_itimer_zero():
    signal.setitimer(signal.ITIMER_REAL, 0, 0)
    print "OK"

#

if sys.platform == 'win32':
    # On Windows, we can only use ITIMER_REAL
    for f in test_itimer_once, test_itimer_repeated:
        f()
    for i in signal.ITIMER_VIRTUAL, signal.ITIMER_PROF:

