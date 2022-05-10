import socket
# Test socket.if_indextoname*
import netifaces
from test.test_support import run_unittest
from test.script_helper import assert_python_ok

from sys import platform
if platform != 'darwin':
    raise unittest.SkipTest("only on Mac")

