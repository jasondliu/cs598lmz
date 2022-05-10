import select
# Test select.select() with a large number of file descriptors.
import sys
import test.support
import time
import unittest
from test.support import TESTFN, unlink, run_unittest
from test.support.script_helper import assert_python_ok
from test.support.script_helper import assert_python_failure
from test.support.script_helper import assert_python_exit_zero
from test.support.script_helper import assert_python_exit_non_zero
from test.support.script_helper import assert_python_ok
from test.support.script_helper import spawn_python

try:
    import threading
except ImportError:
    threading = None

if sys.platform.startswith('freebsd'):
    # FreeBSD's select() implementation can't handle more than 1024 file
    # descriptors.
    MAXFD = 1024
else:
    MAXFD = select.PIPE_BUF

#
# Test the basic operation of the module.
#

class SelectTestCase(unittest.TestCase):

    def
