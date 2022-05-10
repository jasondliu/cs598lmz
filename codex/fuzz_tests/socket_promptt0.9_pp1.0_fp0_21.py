import socket
# Test socket.if_indextoname*
import netifaces
from test.test_support import run_unittest
from test.script_helper import assert_python_ok

from sys import platform
if platform != 'darwin':
    raise unittest.SkipTest("only on Mac")

try:
    socket.if_indextoname(0)
except socket.error, msg:
    # Issue #10302: OSX reports EMSGSIZE if not root.
    raise unittest.SkipTest("failed to get interface index: %r" % msg)

# need root to read /proc/net/dev
out, err, rc = assert_python_ok('-c', 'import netifaces;'\
    'print netifaces.if_nameindex()')

if not rc:
    raise unittest.SkipTest("if_nameindex() failed")

class IfIndexTest(unittest.TestCase):
    """test socket.if_indextoname(if_nameindex()).
    The assumption is that if_nameindex() indexes the same
    interfaces as tested by if_
