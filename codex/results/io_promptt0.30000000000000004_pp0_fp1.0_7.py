import io
# Test io.RawIOBase

import io
import _io
import unittest
import weakref

from test import support

# A mixin for RawIOBase tests that defines a few sample raw byte strings.
class RawIOMixin:
    def setUp(self):
        self.sample_1 = b"ABC"
        self.sample_2 = b"DEF"
        self.sample_3 = b"GHI"
        self.sample_4 = b"JKL"
        self.sample_5 = b"MNO"
        self.sample_6 = b"PQR"
        self.sample_7 = b"STU"
        self.sample_8 = b"VWX"
        self.sample_9 = b"YZ["
        self.sample_10 = b"\\]^_"
        self.sample_11 = b"`abc"
        self.sample_12 = b"defg"
        self.sample_13 = b"hijk"
        self.sample_14 = b"lmno"
        self.sample_15 = b"p
