import socket
# Test socket.if_indextoname function
if socket.if_indextoname(1) != 'eth0':
    fail("socket.if_indextoname(1) != 'eth0'")

# Test socket.if_nameindex function
if socket.if_nameindex()[0] != ('eth0', 1):
    fail("socket.if_nameindex()[1] != ('eth0', 1)")

# End of test case
