import signal
# Test signal.setitimer
# Verifies that signal.setitimer works

# Sanity check: see that signal.alarm raises a signal
def test_signal_alarm():
    signal.setitimer(signal.ITIMER_REAL, 0.001)
    try:
        signal.alarm(1); signal.siginterrupt(signal.SIGALRM, 0); signal.pause()
    except KeyboardInterrupt:
        # alarm signal is ignored because of siginterrupt
        pass
    with pytest.raises(AssertionError):
        for _ in range(3): signal.alarm(1)
    raise AssertionError

