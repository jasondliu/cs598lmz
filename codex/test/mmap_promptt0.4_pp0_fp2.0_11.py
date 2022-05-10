import mmap
# Test mmap.mmap.find
#
# Test for mmap.mmap.find() method.
#
# This test is based on the test for mmap.mmap.find() method from the Python
# 2.6.5 source distribution.
#
# Original test copyright:
#
# Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
# 2011, 2012, 2013, 2014, 2015 Python Software Foundation.  All rights reserved.
#
# Copyright (c) 2000 BeOpen.com.  All rights reserved.
#
# Copyright (c) 1995-2001 Corporation for National Research Initiatives.  All
# rights reserved.
#
# Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.  All
# rights reserved.

# Test for mmap.mmap.find() method.

import unittest
import mmap
import os
import sys
import tempfile

from test import support

# Skip this test if the system's mmap module doesn't have a find() method.

