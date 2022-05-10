import socket
# Test socket.if_indextoname(3)

import unittest
from test import support
from test.support import bigaddr

def get_interface_addresses():
    """
    Get interface addresses and return a mapping
    {name: [addresses]}
    """
    import socket
    import struct
    import fcntl
    import ctypes
    import ctypes.util
    NI_MAXHOST = 1025
    # get interface addresses
    ifnames = socket.if_nameindex()
    if not ifnames:
        raise unittest.SkipTest("No network interfaces found")
    # get addresses
    libc = ctypes.CDLL(ctypes.util.find_library(ctypes.util.find_library('c')))
    NI_MAXHOST = 1025
    sockaddr = ctypes.c_void_p
    socklen_t = ctypes.c_uint32
    sa_family_t = ctypes.c_ushort
