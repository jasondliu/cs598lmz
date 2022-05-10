import mmap
# Test mmap.mmap()
import os
import signal
import sys
# Test sys.argv(), sys.exit(), sys.platform, sys.settrace(), sys.gettrace()
import threading
# Test threading.Thread.__init__() and .run()
import time
# Test time.time()
import traceback
# Test traceback.extract_stack()

from test import test_support

# Test os.times()
if hasattr(os, "times"):
    os_times = os.times
else:
    os_times = None

if test_support.is_jython:
    # Jython has no sys.settrace() at all
    settrace = None
else:
    settrace = sys.settrace

# The name of this test.
_TESTNAME = "test_traceback"

# Don't use a lambda expression, as it is not possible to match the output
# of the function using a regular expression.
def f():
    """This function is called in several different ways by the test script,
    and each call should produce a different traceback."""

