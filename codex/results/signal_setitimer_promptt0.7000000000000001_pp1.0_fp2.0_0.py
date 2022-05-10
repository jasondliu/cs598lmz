import signal
# Test signal.setitimer/alarm
import time
import errno
from test import support
from test.support import find_unused_port
import unittest
from collections import namedtuple
import threading
import weakref
import selectors
import socket
import os
from test.support import os_helper
import sys
import gc
from test.support import import_helper

threading = import_helper.import_module('threading')
thread = import_helper.import_module('thread')

try:
    import resource
except ImportError:
    resource = None

if not hasattr(selectors, "PollSelector"):
    raise unittest.SkipTest("platform does not support PollSelector")

if sys.platform == "win32":
    SETITIMER_ARG_CHECK = selectors.SelectSelector.SETITIMER_ARG_CHECK
else:
    SETITIMER_ARG_CHECK = 0

# On Windows, SIGBREAK is not supported by the signal module.
# On AIX, SIGXFSZ is not supported by the signal module
