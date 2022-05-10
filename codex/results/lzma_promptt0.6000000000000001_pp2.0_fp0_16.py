import lzma
# Test LZMADecompressor.
#
# This test case is based on test_lzma.py from Python 3.4.
#
# Copyright (c) 2014, 2015, 2016, 2017, 2018, 2019, 2020
# Python Software Foundation.  All rights reserved.
#
# Copyright (c) 2010, 2015, 2016, 2017, 2018, 2019, 2020
# by Python Software Foundation.  All rights reserved.
#
# Copyright (c) 2000-2001, 2003-2004, 2006-2008, 2010, 2012, 2014, 2016, 2019
# BeOpen.com.  All rights reserved.
#
# Copyright (c) 1995-2001 Corporation for National Research Initiatives.
# All rights reserved.
#
# Copyright (c) 1991-1995 Stichting Mathematisch Centrum.
# All rights reserved.

import os
import struct
import unittest
from test.support import TESTFN, run_unittest, requires_zlib, requires_bz2
from test.support.script_helper import assert_python_ok
from test.support.script_helper import assert_python_failure
from test.support.temp
