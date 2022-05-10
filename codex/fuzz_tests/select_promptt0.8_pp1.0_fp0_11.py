import select
# Test select.select(...) with lists, with a zero timeout,
# and with a timeout that is too short. (FD_SETSIZE is incorrect,
# so select() returns no error but the specified file
# descriptor is not set in the result.)

from test_support import verify
from test_support import verbose
from test_support import TestFailed

import os
import socket
import select
from select import __file__ as select_file
from socket import __file__ as socket_file
from socket import AF_INET, AF_UNIX, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

# This test uses the maximum allowed timeout value (two floating-point
# seconds) in order to avoid hanging if the implementation has a bug
# in this area.  It also uses a timeout of zero to check that
# select()'s behavior in this case is correct.

TIMEOUT_MAX = 2000000.0
TIMEOUT_ZERO = 0.0

if os.name in ('nt', 'os2'):
    TIMEOUT_MIN = 0.001
else:
    TIMEOUT_
