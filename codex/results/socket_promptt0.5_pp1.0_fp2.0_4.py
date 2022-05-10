import socket
# Test socket.if_indextoname()
#
# This is a test to see if socket.if_indextoname() exists and works.
#
# Author: Chris St. John <chris@stjohnsw.com>
# Date: 2016-01-12

import socket

def test_if_indextoname():
    # get the interface index of eth0
    eth0_index = socket.if_nametoindex("eth0")

    # get the interface name of eth0
    eth0_name = socket.if_indextoname(eth0_index)

    # ensure the interface name is eth0
    assert eth0_name == "eth0", "socket.if_indextoname() failed to return 'eth0' as the interface name of eth0"

def test_if_indextoname_bad_index():
    # try to get the interface name of an invalid interface index
    try:
        socket.if_indextoname(-1)
    except socket.error as e:
        # if we get an error, it should be errno 22 (EINVAL)
        assert
