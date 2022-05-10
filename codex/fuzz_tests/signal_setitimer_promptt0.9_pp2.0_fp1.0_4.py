import signal
# Test signal.setitimer.  Used in testing the interpreter.
# Run with -u all to test that sys.setcheckinterval() works as
# intended.  To keep the test simple, we do not really start a
# timer thread.  We just check that the signal handler gets
# control after every 10 instructions.

def f(n, i=0):
    a = 1
    b = 1
    c = 1
    d = 1
    e = 1
    f = 1
    g = 1
    h = 1
    i+=1
    if i < n:
        (a, b, c, d, e, f, g, h) = f(n, i)
    return a, b, c, d, e, f, g, h

def sighandler(signum, frame):
    if signum != signal.SIGVTALRM:
        print "bad signal number"
        sys.exit(2)
    global count
    count = count - 1
    if count == 0:
        event.set()
        print 'ok'
        sys.exit(0)


#
