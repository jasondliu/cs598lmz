import signal
# Test signal.setitimer throws OSError on unrecognized which
signal.setitimer(signal.ITIMER_PROF, 1.0, 1.0)


# Test that the timer function is passed two floats
def sighandler(*args):
    assert len(args) == 2
    assert isinstance(args[0], float)
    assert isinstance(args[1], float)
    raise AssertionError


signal.signal(signal.SIGALRM, sighandler)
signal.setitimer(signal.ITIMER_REAL, 0.001, 0.001)
# Run the timer for a bit
try:
    for _ in range(100):
        time.sleep(0.001)
except AssertionError:
    pass
# Remove the handler and stop the timer
signal.signal(signal.SIGALRM, signal.SIG_IGN)
