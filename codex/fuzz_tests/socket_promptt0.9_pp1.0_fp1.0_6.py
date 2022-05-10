import socket
# Test socket.if_indextoname on interface which doesn't exist.
# This is one of the tests that would benefit from a testing framework
# which didn't report a failure via a Python exception.
# The test should return a status code and not report success via a
# traceback.
import sys
if sys.platform.startswith('linux'):
    # linux reports 2.6.27 socket.if_indextoname(1000, 'ifname') =>
    # OSError: (22, 'Invalid argument')
    interface_index = 1000
else:
    # mac os x reports socket.if_indextoname(0, 'ifname') =>
    # socket.error: if_indextoname(): invalid if_index 0
    interface_index = 0
socket.if_indextoname(interface_index, 'ifname')
print('Unexpected success')
