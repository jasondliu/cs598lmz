import mmap
# Test mmap.mmap()
#
# This test is derived from the mmap module test suite.
#
# Copyright (C) 2001, 2002 Python Software Foundation; All Rights Reserved
#
# Author: Barry Warsaw
# Contact: email-sig@python.org

import unittest
import os
import mmap
import struct
import tempfile
import sys

from test import test_support

# This test is derived from the mmap module test suite.
#
# Copyright (C) 2001, 2002 Python Software Foundation; All Rights Reserved
#
# Author: Barry Warsaw
# Contact: email-sig@python.org

import unittest
import os
import mmap
import struct
import tempfile
import sys

from test import test_support

# The mmap module is only available on Unix and Windows.
requires_32b = unittest.skipUnless(sys.maxsize <= 2**32,
                                   'test requires a 32-bit platform')

requires_64b = unittest.skipUnless(sys.maxsize > 2**32,
                                   'test requires a 64-bit platform')

