import signal
# Test signal.setitimer() using SIGALRM
if hasattr(signal, "setitimer"):
    class S(Exception):
        pass

    def handler(signum, frame):
        raise S
    signal.signal(signal.SIGALRM, handler)
    # This should not hang: Python has a dedicated timer thread so SIGALRM
    # should be delivered.
    oldval = signal.setitimer(signal.ITIMER_REAL, 0)
    signal.setitimer(signal.ITIMER_REAL, 0)
    if not hasattr(signal, 'ITIMER_MONOTONIC'):
        raise TestFailed('signal.setitimer() test failed')
    try:
        signal.setitimer(signal.ITIMER_REAL, 0.2)
    except S:
        pass
    else:
        raise TestFailed('signal.setitimer() test failed')

    signal.setitimer(signal.ITIMER_REAL, oldval[0])
