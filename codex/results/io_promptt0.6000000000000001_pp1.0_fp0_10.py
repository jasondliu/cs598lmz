import io
# Test io.RawIOBase

import io
import _io
import unittest
import weakref
import os
import sys
import threading
import warnings
import contextlib
from test import support
from test.support import threading_helper

import io
import _io
import unittest
import weakref
import os
import sys
import threading
import warnings
import contextlib
from test import support
from test.support import threading_helper

# Issue #19401: If a child thread keeps a reference to an open file
# object, a crash can occur in the parent thread when the file is
# closed and the GC collects the open file object in the child thread.
class FileCrashTest(unittest.TestCase):

    def test_close_in_thread(self):
        # File object is closed in a separate thread
        f = open(support.TESTFN, "wb")
        r = weakref.ref(f)
        def target():
            f.close()
        t = threading.Thread(target=target)
        t.start()
        t.join()
        self.assert
