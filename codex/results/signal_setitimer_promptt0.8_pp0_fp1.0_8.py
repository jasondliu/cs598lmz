import signal
# Test signal.setitimer()
    def handler(signum, frame):
        "Callback invoked when a timer expires"
        print 'Signal handler called with signal', signum
        raise IOError("Timeout reached")
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 0.005)
    print "Before"
    try:
        for i in range(100000):
            pass
        print "After"
    except IOError,err:
        print "Caught:",err
        print "Continuing"
# Test signal.getsignal()
    print "SIGALRM handler is",signal.getsignal(signal.SIGALRM)
    signal.signal(signal.SIGALRM, signal.SIG_DFL)
# Test signal.setitimer() again
    signal.setitimer(signal.ITIMER_REAL, 0.005)
    print "Before"
    time.sleep(0.2)
    print "After"

if __name__ == "__
