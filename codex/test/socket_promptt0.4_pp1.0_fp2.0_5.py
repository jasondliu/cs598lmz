import socket
# Test socket.if_indextoname()
if_indextoname = socket.if_indextoname

import os
import sys
import fcntl
import struct

def test_if_indextoname():
    if sys.platform.startswith('linux'):
        # get the interface name from a known interface index
        index = 1
        interface = if_indextoname(index)
        assert interface == 'lo'
        # get the interface index from a known interface name
        index = if_nametoindex(interface)
        assert index == 1
        # get the interface name from an unknown interface index
        try:
            if_indextoname(index+1)
        except socket.error:
            pass
        else:
            raise AssertionError('if_indextoname() did not fail')
    else:
        # get the interface name from a known interface index
        index = 1
        interface = if_indextoname(index)
        assert interface == 'lo0'
        # get the interface index from a known interface name
