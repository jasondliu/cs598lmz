import signal
# Test signal.setitimer and signal.getitimer

from test.support import run_unittest, get_attribute
from test.support import verbose, import_module, cpython_only
from test.script_helper import assert_python_ok

from time import sleep
import os
import sys

# Windows only supports ITIMER_REAL
ITIMERS = [signal.ITIMER_REAL]

try:
    import _testcapi
    if get_attribute(signal, "ITIMER_REAL") == 0:
        # If we define ITIMER_REAL, we should also define ITIMER_VIRTUAL
        # and ITIMER_PROF, since the value of ITIMER_REAL is 0.
        ITIMERS.append(signal.ITIMER_VIRTUAL)
        ITIMERS.append(signal.ITIMER_PROF)
except ImportError:
    _testcapi = None


@cpython_only
class ItimerTest(unittest.TestCase):
    FUNC = 'alarm_handler'

   
