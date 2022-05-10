import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0, 0)
# Test signal.getitimer
signal.getitimer(signal.ITIMER_REAL)

# Test signal.set_wakeup_fd
signal.set_wakeup_fd(-1)

# Test the SIG_DFL and SIG_IGN constants
signal.SIG_DFL
signal.SIG_IGN

# Issue #11471: test the handlers for signals valid on the platfom.
for sig in [x for x in dir(signal) if x.startswith('SIG')]:
    try:
        signum = getattr(signal, sig)
        if signum == 0:
            continue
        signal.getsignal(signum)
    except ValueError:
        pass
    except AttributeError:
        pass

try:
    signal.pthread_kill
except AttributeError:
    pass
else:
    # Issue #20959: test that pthread_kill raises an exception
    # when given an invalid thread
