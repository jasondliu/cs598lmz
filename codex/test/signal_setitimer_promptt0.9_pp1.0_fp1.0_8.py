import signal
# Test signal.setitimer()
if hasattr(signal, "setitimer"):
    import time
    from time import time
    #def handler(signum, frame):
    #    print "func=%s, signum=%d" % (handler.__name__, signum)
    #signal.signal(signal.SIGPROFPFPFPFPPFPFPFP, handler)
