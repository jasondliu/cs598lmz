import signal
# Test signal.setitimer() on Linux

import unittest
from test.support import check_impl_detail
from test.support.script_helper import assert_python_ok

has_itimer = hasattr(signal, "setitimer")

@unittest.skipUnless(has_itimer, 'Needs setitimer()')
class ItimerTest(unittest.TestCase):

    def test_itimer_error(self):
        # Issue #24178: setitimer() should raise OSError, not OSError(EFAULT)
        with self.assertRaises(OSError) as cm:
            signal.setitimer(signal.ITIMER_PROF, 0.0, 0.0, object())
        self.assertNotIsInstance(cm.exception, OSError)
        self.assertEqual(cm.exception.errno, signal.EFAULT)

