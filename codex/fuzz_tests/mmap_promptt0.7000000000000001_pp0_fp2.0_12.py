import mmap
# Test mmap.mmap(-1, 0)
# https://bugs.python.org/issue37797
import os
import os.path
import signal
import socket
import struct
import sys
import tempfile
import threading
import time
import unittest
import uuid
import weakref

import _testcapi

from test import support
import test.support.script_helper
from test import script_helper

if support.is_jython:
    # Skip this test on Jython, because it's not supported.
    raise unittest.SkipTest("sysv_ipc not supported by jython")

# Some of these tests rely on the system's semaphore limits.  The
# following defines the minimum amount of semaphores required for
# these tests.  If SEM_NSEMS_MAX is sufficiently large, these
# constants can be increased to provide even better testing.
SEMAPHORE_MIN = 5
SEMAPHORE_MAX = 25

# Some of these tests rely on the system's shared memory limits.  The
# following defines the minimum amount of shared memory required for
# these tests.
