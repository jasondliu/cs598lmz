import signal
# Test signal.setitimer and signal.alarm
import time
import unittest

from test.support import (run_unittest, cpython_only, captured_output,
                          requires_linux_version)


class AlarmTest(unittest.TestCase):
    # Issue #8190: alarm() could raise an exception while the signal
    # handler is running, which isn't safe.
    def test_alarm_in_handler(self):
        with captured_output("stderr") as stderr:
            old_alarm = signal.signal(signal.SIGALRM, lambda: (
                                                    signal.alarm(1),
                                                    0,
                                                    1/0))
            signal.alarm(1)
            time.sleep(2)
            self.assertEqual(stderr.getvalue(), "")
        signal.signal(signal.SIGALRM, old_alarm)

    def test_itimer_exception_during_handling_not_swallowed(self):
        with captured_output("stderr") as st
