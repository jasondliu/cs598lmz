import signal
# Test signal.setitimer()
#
# This test is based on the test program from the Python 2.7.3 source
# distribution, Lib/test/test_signal.py.
#
# Copyright (c) 2001-2011 Python Software Foundation; All Rights Reserved
# Copyright (c) 2000 BeOpen.com.
# Copyright (c) 1995-2001 Corporation for National Research Initiatives.
# Copyright (c) 1995-2001 CNRI.  All rights reserved.
#
# Portions of this test module were originally written by Jeff Bauer,
# and later modified by Barry Warsaw and Thomas Wouters.
#
# ***** END LICENSE BLOCK *****

# This test is not run automatically.  Run it manually with:
#
#     python test_signal.py

import os
import sys
import signal
import time
import unittest

from test import test_support

# On OSX, alarm() is a no-op.
alarm_is_not_implemented = (sys.platform == 'darwin')

#
# Test alarm()
#

def alarm_received(signum, frame):
