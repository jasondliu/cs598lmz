import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import _io

# Base class for testing a RawIOBase implementation.
class TestRawIOBase(object):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        self.files = []

    def tearDown(self):
        for name in self.files:
            os.unlink(name)
        os.rmdir(self.tempdir)

    def make_file(self, contents):
        fd, name = tempfile.mkstemp(dir=self.tempdir)
        os.write(fd, contents)
        os.close(fd)
        self.files.append(name)
        return name

    def test_read(self):
        # Read at various positions, from various sizes, with and without
        # a short read at the end.
        for n in range(1, 20):
            for start in range(n):
                for end in range(start, n):
                    for shortread in [False,
