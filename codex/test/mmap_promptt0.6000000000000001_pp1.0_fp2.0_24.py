import mmap
# Test mmap.mmap
#
# Written by: Konrad Hinsen <hinsen@cnrs-orleans.fr>
# Last revision: 1997-11-6
#

import unittest
import sys
import os
import tempfile
import mmap
import struct

if hasattr(os, 'O_BINARY'):
    O_BINARY = os.O_BINARY
else:
    O_BINARY = 0

class MMapTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = tempfile.mktemp()
