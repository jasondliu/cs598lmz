import signal
# Test signal.setitimer() and SIGPROF, SIGALRM

# XXXX This test is known to fail on platforms where PyOS_Nanoseconds()
# XXXX doesn't return times measured in nanoseconds.

import errno
import os
import select
import struct
import sys
import time
import unittest
from test.support import (TestFailed, run_with_locale, find_unused_port,
                          run_unittest, get_attribute, cpython_only,
                          reap_children)
from test.script_helper import assert_python_ok
from io import StringIO
import subprocess

try:
    import threading
except ImportError:
    threading = None

try:
    import ssl
except ImportError:
    ssl = None

try:
    import termios
except ImportError:
    termios = None

try:
    import resource
except ImportError:
    resource = None

SIGCHLD = getattr(signal, "SIGCHLD", None)

HOST = 'localhost'
HOST
