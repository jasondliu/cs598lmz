import io
# Test io.RawIOBase
#
# This tests the RawIOBase implementation of the io module.
# Note that the io module provides an abstract base class
# for Raw I/O, so normally you would not import it directly.
#
# Written by Amaury Forgeot d'Arc and Antoine Pitrou

import os
import sys
import unittest
import io

from test import support

try:
    import threading
except ImportError:
    threading = None

# Base class for testing IO objects
class BaseTestRawIO(object):
    # Subclass must define the following:
    # - self.filename
    # - self.mode
    # - self.btype (bytes or bytearray)
    # - self.modes (all possible modes)

    def setUp(self):
        # Create test file
        fp = open(self.filename, 'wb')
        try:
            fp.write(b'abcdefghijklmnopqrstuvwxyz\n')
            fp.write(b'012345678901234567890123
