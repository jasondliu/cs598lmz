import signal
# Test signal.setitimer(), signal.getitimer()
from test import support
from test.support import os_helper
from test.support import reap_threads
import unittest
from time import time, sleep
import errno
from functools import partial
try:
    import threading
except ImportError:
    threading = None
from test.support.script_helper import assert_python_ok, assert_python_failure

is_jython = sys.platform.startswith('java')
is_android = sys.platform.startswith('android')
is_netbsd = sys.platform.startswith('netbsd')

# Don't test the itimer if it is not supported
# (e.g. FreeBSD doesn't support ITIMER_VIRTUAL)
if is_jython or is_android or is_netbsd:
    raise unittest.SkipTest("test is not supported on this platform")

