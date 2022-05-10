import signal
# Test signal.setitimer or signal.setitimer() only.
try:
    t = signal.getitimer(signal.ITIMER_VIRTUAL)
except AttributeError:
    raise unittest.SkipTest("Platform does not support itimers")


@unittest.skipUnless(hasattr(signal, 'setitimer'), "setitimer is not implemented")
class ItimerTestCase(unittest.TestCase):

    @unittest.skipUnless(hasattr(signal, 'setitimer'),
        'setitimer() required for this test.')
    def test_itimer_zero(self):
        for which in [signal.ITIMER_VIRTUAL, signal.ITIMER_PROF,
            signal.ITIMER_REAL]:
            self.assertGreaterEqual(signal.getitimer(which), (0, 0))
            itimer = signal.setitimer(which, 0)
            self.assertGreaterEqual(signal.getitimer(which), (0, 0))
            itimer = signal.setitimer
