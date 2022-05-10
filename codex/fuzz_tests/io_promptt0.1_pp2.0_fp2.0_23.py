import io
# Test io.RawIOBase

import unittest
from test import support
from io import BytesIO, BufferedReader, BufferedWriter, BufferedRWPair
from io import BufferedRandom, TextIOWrapper
import os
import sys
import tempfile
import weakref
import warnings

# Base class for testing a raw IO implementation
class BaseRawIOIntTests(object):
    # Subclass must define the following attributes:
    # - self.filename
    # - self.mode
    # - self.b1
    # - self.b2
    # - self.b3
    # - self.b4
    # - self.b5
    # - self.b6
    # - self.b7
    # - self.b8
    # - self.b9
    # - self.b10
    # - self.b11
    # - self.b12
    # - self.b13
    # - self.b14
    # - self.b15
    # - self.b16
    # - self.b17
    # - self.b18
   
