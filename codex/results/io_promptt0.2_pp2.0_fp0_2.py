import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import warnings

from test import support
from test.support import import_module

# Base class for testing a RawIOBase implementation.
# Subclasses must override read(), readinto() and seek(),
# and set the class attributes name, type2test and type2test_memoryview.
class RawIOTest:
    name = None
    type2test = None
    type2test_memoryview = None

    def setUp(self):
        self.f = self.type2test(self.name)
        self.f2 = self.type2test(self.name)
        self.f3 = self.type2test(self.name)
        self.f4 = self.type2test(self.name)

    def tearDown(self):
        if self.f:
            self.f.close()
        if self.f2:
            self.f2.close()
        if self.f3:
            self.f3.close()
        if self.f
