import signal
# Test signal.setitimer() in a few modes.
from test import support
signal_names = {s: k for k, s in signal.__dict__.items() if k.startswith('SIG')}
import subprocess
import sys
import time
import unittest
IS_64_BITS = sys.maxsize > 2 ** 32


def handler(signum, frame):
    frame.f_locals['caught'] = signum


class TestSignal(unittest.TestCase):

    def test_default_int_handler(self):
        with captured_output('stderr') as output:
            os.kill(os.getpid(), signal.SIGINT)
        self.assertEqual(output.getvalue(), '\n')

    def test_signal(self):
        caught = []

        def alarm_handler(signum, frame):
            caught.append(signum)
            self.assertIsNotNone(signum)
            self.assertIsNotNone(frame)

        signal.signal(signal.SIGALRM, alarm_handler)
       
