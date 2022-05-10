import signal
# Test signal.setitimer() under Linux and FreeBSD.
import sys
import unittest
from test.support import run_unittest, cpython_only, check_impl_detail, import_helper


@cpython_only
class ItimerTestCase(unittest.TestCase):

    def _alarm_handler(self, signum, frame):
        self.alarm_fired = True

    def _test_itimer(self, timer_type, interval, duration, itimer_id=-1):
        if hasattr(signal, 'ITIMER_' + timer_type):
            timer_type = getattr(signal, 'ITIMER_' + timer_type)
        if itimer_id == -1:
            itimer_id = timer_type
        self.alarm_fired = False
        original_handler = signal.signal(signal.SIGALRM, self._alarm_handler)
        signal.setitimer(itimer_id, interval, duration)
        time.sleep(interval + duration)
        # Restore the original signal handler
        signal.signal
