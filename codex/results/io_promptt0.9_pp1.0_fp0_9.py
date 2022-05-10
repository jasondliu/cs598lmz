import io
# Test io.RawIOBase for readability exception handling.

import os
import unittest
import weakref
try:
    import threading
except ImportError:
    threading = None

from test.support import (captured_output, findfile,
                          gc_collect, import_module,
                          captured_stdout, run_with_locale)


# Misc tests related to I/O.

class TestIo(unittest.TestCase):
    class ClosingFile:
        closed = 0
        def close(self):
            self.closed = 1

    def testWeakrefs(self):
        f = self.ClosingFile()
        p = weakref.proxy(f)
        self.assertEqual(p.closed, 0)
        f.close()
        self.assertEqual(p.closed, 1)

    def test_abc(self):
        self.assertIs(io.IOBase, io.RawIOBase)

    def test_io_open(self):
        # Issue 13777: io.open should work as os.fdopen
        self.
