import lzma
# Test LZMADecompressor
#
# This file is part of the pyxwf library, released under the BSD license.
# The full license is in the file COPYING, distributed as part of this software.
#
# Copyright (c) 2011, 2012, 2013, 2014, 2015, 2016 The University of Queensland
#

import os
import sys
import tempfile
import unittest
import subprocess
import shutil

from pyxwf.utils.compression import LZMADecompressor, LZMAEncoder

#
# This is a test of the LZMADecompressor class.
#
# It is a bit of a hack, and relies on the availability of the
# lzma command line utility.
#

class TestLZMADecompressor(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.tmpdir_path = os.path.abspath(self.tmpdir)
        self.tmpfile = os.path.join(self.tmpdir_path, "test.lzma
