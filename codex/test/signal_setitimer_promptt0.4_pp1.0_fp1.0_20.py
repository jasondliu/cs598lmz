import signal
# Test signal.setitimer() with SIGALRM

from test.support import run_unittest, get_attribute, verbose
from test.support.script_helper import assert_python_ok

import os
import sys
import time
import unittest
from time import sleep
from test.support import os_helper

# Skip these tests if the platform does not have setitimer().
if not hasattr(signal, 'setitimer'):
    raise unittest.SkipTest("platform does not have setitimer()")

# Skip these tests if the platform does not have SIGALRM.
if not hasattr(signal, 'SIGALRM'):
    raise unittest.SkipTest("platform does not have SIGALRM")

# Skip these tests if the platform does not have SIGPROF.
if not hasattr(signal, 'SIGPROF'):
    raise unittest.SkipTest("platform does not have SIGPROF")

# Skip these tests if the platform does not have SIGVTALRM.
