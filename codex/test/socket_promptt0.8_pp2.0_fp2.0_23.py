import socket
# Test socket.if_indextoname.

def check(family, expected_name):
    # Get the ifname of the loopback interface.
    ifname = socket.if_indextoname(1)
