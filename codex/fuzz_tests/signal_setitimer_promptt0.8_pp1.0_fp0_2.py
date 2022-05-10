import signal
# Test signal.setitimer and associated functions.
# Old integer-based timer interface.
# This test is not very useful without SIGALRM.
with mock.patch('signal.setitimer', create=True) as mock_setitimer:
    signal.setitimer(signal.ITIMER_REAL, 0.0)
    assert mock_setitimer.mock_calls == [mock.call(signal.ITIMER_REAL, 0.0)], mock_setitimer.mock_calls
    signal.setitimer(signal.ITIMER_PROF, 0.0, 0.0)
    assert mock_setitimer.mock_calls == [mock.call(signal.ITIMER_REAL, 0.0), mock.call(signal.ITIMER_PROF, 0.0, 0.0)], mock_setitimer.mock_calls
    signal.setitimer(signal.ITIMER_VIRTUAL, 0.0, 0.0)
    assert mock_setitimer.mock_calls ==
