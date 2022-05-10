import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = None
    def open(self):
        self.file = open(self.name, 'rb')
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def readinto(self, b):
        return self.file.readinto(b)
    def __repr__(self):
        return '<File name={!r}>'.format(self.name)

import os
import sys
import tempfile
import unittest
import weakref

from test import support

class AutoFileTests(unittest.TestCase):

    def setUp(self):
        self.name = support.TESTFN
        self.file = File(self.name)
        self.file.open()

    def tearDown(self):
        self.file.close()
        support.unlink(self.name)

    def test_weakref(self):
        p = weakref.proxy(self.file
