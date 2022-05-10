import signal
# Test signal.setitimer()

import os
import sys
import time
import threading
import signal
import unittest
from test.support import run_unittest, verbose, import_module
thread = import_module('thread')

# This test is Linux-specific.
if sys.platform != 'linux':
    raise unittest.SkipTest("test specific to Linux")

# This test is Linux-specific.
if hasattr(signal, 'alarm'):
    raise unittest.SkipTest("test specific to Linux")

# This test is Linux-specific.
if not hasattr(signal, 'setitimer'):
    raise unittest.SkipTest("test specific to Linux")

# This test is Linux-specific.
if hasattr(signal, 'set_wakeup_fd'):
    raise unittest.SkipTest("test specific to Linux")

# This test is Linux-specific.
if hasattr(signal, 'siginterrupt'):
    raise unittest.SkipTest("test specific to Linux")

# This test is Linux-specific.
