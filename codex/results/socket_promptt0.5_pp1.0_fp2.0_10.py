import socket
# Test socket.if_indextoname()

import sys
import unittest
from test import support
from test.support import find_unused_port, TESTFN
from test.support.script_helper import assert_python_ok

from socket import socketpair, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_BINDTODEVICE

# If a network interface is not present, if_indextoname() returns None.
# We try to find an interface that is not present.

def test_if_indextoname():
    interface_name = None
    # get all interfaces
    interfaces = socket.if_nameindex()
    # loop over interfaces
    for interface in interfaces:
        try:
            # try to get the name of the interface
            interface_name = socket.if_indextoname(interface[0])
        except ValueError:
            # the interface does not exist
            break
    # if the interface exists, we must be able to get its name
    if interface_name is not None:
        raise ValueError("Could not find a non-existent interface")


