import signal
# Test signal.setitimer(), calls signal.setitimer(), signal.getitimer() with
# the different timer signals, attempt to check that they work correctly
import time
import unittest


class UtimeTest:

    def test_setitimer_getitimer(self):
        interval = 0.1
        iterations = 5
        t = time.time()
        for i in range(1, iterations):
            signal.setitimer(signal.ITIMER_VIRTUAL, interval, 0)
            time.sleep(interval)
        signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)
        self.assertEqual(time.time(), t + interval * iterations,
            'setitimer behaves incorrectly')
        self.assertEqual(signal.getitimer(signal.ITIMER_VIRTUAL), (
            0.0, 0.0), 'getitimer behaves incorrectly')


