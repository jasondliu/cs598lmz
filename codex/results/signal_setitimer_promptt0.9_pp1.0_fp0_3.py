import signal
# Test signal.setitimer(2) with a timer value of zero on the
# SIGALRM signal to deactivate the timer.
from test import support
import time
import unittest


class TimeValTest(unittest.TestCase):

    def test_zero_time_val(self):


        def alarm_received(signum, frame):
            self.fail('SIGALRM received')
        self.contained_alarm = alarm_received
        old_handler = signal.signal(signal.SIGALRM, self.contained_alarm)
        try:
            signal.setitimer(signal.ITIMER_REAL, 0)
            support.run_with_pep479(self, support.TESTFN,
                lambda : None, lambda : None)
        finally:
            signal.signal(signal.SIGALRM, old_handler)


def test_main():
    support.run_unittest(TimeValTest)


if __name__ == '__main__':
    test_main()
