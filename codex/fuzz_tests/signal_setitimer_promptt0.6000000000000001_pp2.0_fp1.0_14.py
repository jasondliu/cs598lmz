import signal
# Test signal.setitimer()
class TestSetitimer:

    def test_setitimer(self):
        signal.setitimer(signal.ITIMER_REAL, 1, 0)
        assert signal.getitimer(signal.ITIMER_REAL) == (1, 0)
        signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)
        assert signal.getitimer(signal.ITIMER_VIRTUAL) == (1, 0)
        signal.setitimer(signal.ITIMER_PROF, 1, 0)
        assert signal.getitimer(signal.ITIMER_PROF) == (1, 0)

    def test_setitimer_error(self):
        raises(TypeError, signal.setitimer, signal.ITIMER_REAL, 1j, 0)
        raises(TypeError, signal.setitimer, signal.ITIMER_REAL, 1, 1j)
        raises(ValueError, signal.setitimer, -1, 1, 1)

# Test signal.gets
