import signal
# Test signal.setitimer()
if hasattr(signal, "setitimer"):
    import time
    from time import time
    #def handler(signum, frame):
    #    print "func=%s, signum=%d" % (handler.__name__, signum)
    #signal.signal(signal.SIGPROFPFPFPFPPFPFPFP, handler)
    print "start =", time()
    signal.setitimer(signal.ITIMER_VIRTUAL, 0.001, 1)
    while True:
        print "end=%s" % (time() - start,)
        signal.pause()
    signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)

sys.exit(rc)
