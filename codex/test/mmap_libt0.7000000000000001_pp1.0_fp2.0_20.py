import mmap
import os
import socket
import struct
import sys
import tempfile
import threading
import time
import traceback
import types
import unittest

from test import support
from test.support import TESTFN, run_unittest, check_warnings, import_module
from test.support.script_helper import assert_python_ok

import _testcapi

# Tell the test harness we have a third thread running.
threading.current_thread().name = 'MainThread'

HOST = support.HOST
