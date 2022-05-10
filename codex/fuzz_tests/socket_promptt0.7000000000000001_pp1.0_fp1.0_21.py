import socket
# Test socket.if_indextoname()
import socket
from socket import if_indextoname
import os

if os.name == 'nt':
    # These tests do not work under Windows.
    print('Test skipped under Windows')
    raise SystemExit

# Under Linux, if_indextoname() requires root privileges.

# This test requires root privileges.
import sys
if os.getuid() != 0:
    print('Test skipped: must be run as root')
    sys.exit(0)

# Test the function.

if if_indextoname(1) != 'lo':
    print('if_indextoname(1) failed')

try:
    if_indextoname(0)
except ValueError:
    pass
else:
    print('if_indextoname(0) failed to raise a ValueError')
