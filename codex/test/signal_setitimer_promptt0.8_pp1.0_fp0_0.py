import signal
# Test signal.setitimer
from test import support

support.RequiresIsolatedTempdir()


class Alarm(Exception):
    pass


def alarm_handler(signum, frame):
    signal.setitimer(signal.ITIMER_REAL, 0)
    raise Alarm


def test_setitimer_real(self):
    # Test alarm using setitimer
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, 0.1)
    try:
        signal.pause()
    except Alarm:
        pass
    else:
        self.fail("didn't get Alarm")


class TestSetitimer(unittest.TestCase):
    @unittest.skipIf(not hasattr(signal, 'setitimer'),
                     'setitimer not available')
    def test_setitimer_real(self):
        test_setitimer_real(self)


def test_main():
    support.run_unittest(TestSetitimer)



