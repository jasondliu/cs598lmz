import lzma
# Test LZMADecompressor.decompress() method
#
# This test is based on
# https://github.com/python/cpython/blob/master/Lib/test/test_lzma.py
#
# Copyright (c) 2004-2020 Python Software Foundation; All Rights Reserved
# Copyright (c) 2001-2020 Python Software Foundation; All Rights Reserved
#
# Author: Victor Stinner

import unittest
import io
import os
import struct
import sys
import tempfile
import warnings
from test import support
