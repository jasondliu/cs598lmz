import signal
# Test signal.setitimer() function
# This function is only available on UNIX
setitimer = getattr(signal, "setitimer", None)
if setitimer is not None:
    funcname = "setitimer"
    func_args = []
    func_return = []
    def cleanup(sig, frame):
        pass

    sig = signal.SIGALRM
    pre_value = 5000

    print('*** Testing %s ***' % funcname)
    try:
        setitimer(signal.ITIMER_REAL, pre_value)
        t = time.time()
        a = 0
        signal.signal(sig, cleanup)
        for i in range(100):
            a += i
        t = time.time() - t
        value = t * 1000
        setitimer(signal.ITIMER_REAL, 0)
        if abs(value - pre_value) < 20: # 20 ms tolerance
            print('%s %r' % (funcname, (value,)))
        else:
            raise ValueError('%s returned %r
