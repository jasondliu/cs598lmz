import socket
# Test socket.if_indextoname
# if_indextoname is a function that takes the index of an interface as a
# parameter and returns its name.

# This test is dependent on an active network interface.

import support

# We need to have an active network interface for this test
if not game.IsOnline():
    raise support.TestSkipped("Not connected to the Internet.")

ifname = socket.if_indextoname(1)
print ifname
