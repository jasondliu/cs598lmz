import signal
# Test signal.setitimer()

# Copyright (C) 2001-2016 Python Software Foundation; All Rights Reserved

import unittest
import os
import sys
import time
import signal

from test.support import run_unittest, run_with_locale, unlink, import_module

thread = import_module('thread')

# Skip tests if setitimer() is not available.
try:
    signal.setitimer(signal.ITIMER_REAL, 0, 0)
except AttributeError:
    raise unittest.SkipTest("setitimer not available")

# Skip tests if SIGALRM is not available.
try:
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
except ValueError:
    raise unittest.SkipTest("SIGALRM not available")

# Skip tests if SIGUSR1 is not available.
try:
    signal.signal(signal.SIGUSR1, signal.SIG_IGN)
except ValueError:
    raise unittest.SkipTest("SIGUSR1 not available")
