import signal
# Test signal.setitimer

def test_returns_none():
    assert signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2) is None

def test_fails_when_unknown_timer_argument():
    with raises(ValueError):
        signal.setitimer(1, 0.2, 0.2)

def test_fails_when_less_than_zero_float():
    with raises(ValueError):
        signal.setitimer(signal.ITIMER_REAL, -1.0, 0.2)

def test_if_returns_time_until_alarm_in_float():
    alarm = alarm - time.time()
    assert alarm == 0.0

def test_if_returns_interval_in_float():
    interval = interval - time.time()
    assert interval == 0.2
