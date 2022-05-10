import signal
# Test signal.setitimer
if hasattr(signal, 'setitimer'):
    def handler(*args):
        raise KeyboardInterrupt
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 0.5)
    try:
        exec("1 + 1")
    except KeyboardInterrupt:
        pass

    def handler(*args):
        raise SystemExit
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 0.001)
    try:
        exec("1 + 1")
    except SystemExit:
        pass

# Test signal.siginterrupt
# siginterrupt() is not available on Solaris
# or on OS/2.
if hasattr(signal, 'siginterrupt'):
    if hasattr(signal, 'SIGBREAK'):
        signal.siginterrupt(signal.SIGBREAK, False)
