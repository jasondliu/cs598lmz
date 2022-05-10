import signal
# Test signal.setitimer, possibly including the optional itimer_which argument.
if hasattr(signal, 'setitimer'):
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    signal.setitimer(signal.ITIMER_REAL, 0.5, 1.0)
    signal.setitimer(signal.ITIMER_REAL, 1.0)
    signal.setitimer(signal.ITIMER_REAL, 0)
    if hasattr(signal, 'ITIMER_PROF'):
        signal.setitimer(signal.ITIMER_PROF, 0.5, 1.0)
        signal.setitimer(signal.ITIMER_PROF, 1.0)
        signal.setitimer(signal.ITIMER_PROF, 0)
    if hasattr(signal, 'ITIMER_VIRTUAL'):
        signal.setitimer(signal.ITIMER_VIRTUAL, 0.5, 1.0)
        signal.setitimer(sign
