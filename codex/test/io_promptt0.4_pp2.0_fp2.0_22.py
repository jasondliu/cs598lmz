import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import os
import errno
import sys
import io
import tempfile
import stat

# Base class for testing RawIOBase.
# This tests the read(), readinto() and readall() methods,
# as well as seek(), tell() and truncate()
# It doesn't test write(), writelines() or detach()
class BaseRawTests(object):
    # Subclass must define the following attributes:
    # f
    # t
    # support_seek

    # Subclass may define the following attributes:
    # truncate_unsupported

    def test_read(self):
        self.assertEqual(self.f.read(0), b(""))
        self.assertEqual(self.f.read(1), self.t("a"))
        self.assertEqual(self.f.read(2), self.t("bc"))
        self.assertEqual(self.f.read(5), self.t("d"))
        self.assertEqual(self.f.read(1), b(""))


