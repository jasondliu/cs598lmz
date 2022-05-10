import signal
# Test signal.setitimer()
#
# This test is derived from test_signal.py.
#
# Copyright (C) 2001-2003 Python Software Foundation.
# Written by Neal Norwitz.

import unittest
import sys
import time
import os

from test.support import run_unittest, reap_children, get_attribute

# Skip this test if the implementation doesn't provide setitimer().
setitimer = get_attribute(signal, 'setitimer')
if not setitimer:
    raise unittest.SkipTest("platform doesn't support setitimer()")

# Skip this test if the implementation doesn't provide ITIMER_REAL.
ITIMER_REAL = get_attribute(signal, 'ITIMER_REAL')
if not ITIMER_REAL:
    raise unittest.SkipTest("platform doesn't support ITIMER_REAL")

# Skip this test if the implementation doesn't provide SIGALRM.
SIGALRM = get_attribute(signal, 'SIGALRM')
if not SIGALRM:
    raise unittest.
