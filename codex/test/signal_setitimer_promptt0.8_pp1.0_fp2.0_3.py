import signal
# Test signal.setitimer() for SIGVTALRM.
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)
# Test signal.setitimer() for SIGPROF.
signal.setitimer(signal.ITIMER_PROF, 1, 0)

# Test signal.set_wakeup_fd()
if not hasattr(signal, 'set_wakeup_fd'):
    try:
        signal.set_wakeup_fd(-5)
    except ValueError:
        pass
    else:
        raise ValueError
    try:
        signal.set_wakeup_fd(0)
    except OSError:
        pass
    else:
        raise OSError
    try:
        signal.set_wakeup_fd(1000000)
    except OSError:
        pass
    else:
        raise OSError
signal.set_wakeup_fd(1)
signal.set_wakeup_fd(2)
signal.set_wakeup_fd(3)
