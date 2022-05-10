import signal
# Test signal.setitimer() and signal.getitimer().
# XXX: coverage.py hangs when using signal.setitimer() and signal.getitimer()
# under coverage measurement.
# This is a known issue: http://bitbucket.org/ned/coveragepy/issue/85/cant-use-setitimer-or-alarm-in-measurements
@pytest.mark.skipif(coverage is not None, reason="known coverage.py issue #85")
LIMIT = 0.01
def handler(signum, frame):
    "signal handler function does nothing."
    pass
def snooze_with_signal(secs):
    "Snooze with signal."
    old = signal.signal(signal.SIGALRM, handler)
    try:
        signal.setitimer(signal.ITIMER_REAL, secs)
        signal.pause()
    finally:
        signal.signal(signal.SIGALRM, old)
def test_signal_setitimer():
    "Test signal.setitimer()."
   
