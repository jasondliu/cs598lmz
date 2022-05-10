import socket
# Test socket.if_indextoname()
#
# The socket.if_indextoname() function is supposed to return the name of the
# interface specified by index.
#
# The test creates a socket, gets the name of the interface, gets the index of
# the interface and then gets the name of the interface again.
#
# The test checks that the two names are the same.
import os
import sys
import unittest
import platform
import subprocess
from test import support

def get_interface_name():
    # Get the name of the interface to use for this test.
    #
    # This test uses the first interface that is not the loopback interface.
    #
    # This is the same approach used by test_socket.test_getservbyport().
    interfaces = socket.if_nameindex()
    for interface in interfaces:
        if interface[1] != 'lo':
            return interface[1]
    return None

@unittest.skipUnless(hasattr(socket, "if_indextoname"),
                     'if_indextoname() required')
@unittest.skipUnless
