import select
# Test select.select with a timeout.
# On Windows, select() doesn't work with non-blocking pipes,
# so skip this test there.
# Also, on Windows, select() doesn't work with sockets, so skip that
# part of the test as well.
import sys
if sys.platform != 'win32':
    import os
    import socket
    import time
    import unittest
    import threading

    from test.support import TESTFN, unlink


    class SelectTestCase(unittest.TestCase):
        @unittest.skipUnless(hasattr(select, 'poll'), 'test needs select.poll')
        def test_select_with_poll(self):
            # Issue #16500: select() must not return a fd for a closed file
            # descriptor, even if it has been registered in select.poll().
            # This is a regression test for http://bugs.python.org/issue16500
            fd = os.open(TESTFN, os.O_CREAT | os.O_WRONLY, 0o600)
