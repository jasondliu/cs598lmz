import signal
# Test signal.setitimer
# See http://bugs.python.org/issue13603
signal.setitimer(signal.ITIMER_REAL, 0, 0.5)
assert signal.setitimer(signal.ITIMER_PROF, 0, 0.5) == (0.0, 0.0)
assert signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0.5) == (0.0, 0.0)
# CPython raises ValueError for an invalid signal
try:
    signal.setitimer(signal.SIGUSR1, 0, 0.5)
except ValueError:
    pass
else:
    assert False, "expected ValueError"
try:
    signal.setitimer(signal.NSIG, 0, 0.5)
except ValueError:
    pass
else:
    assert False, "expected ValueError"

# Test signal.signal()
signal.signal(signal.SIGCHLD, signal.SIG_DFL)
# CPython checks that the signal is valid
