import socket
# Test socket.if_indextoname()
#
# This test is just a basic sanity check.  It doesn't check if the function
# actually does what it's intended to do.  It also doesn't check for all
# possible error conditions.

if_indextoname = socket.if_indextoname

# Test a valid interface index.
index = socket.if_nametoindex("lo")
name = if_indextoname(index)
if name != "lo":
    raise TestFailed("if_indextoname() returned %s, expected lo" % name)

# Test an invalid interface index.
try:
    if_indextoname(0)
except ValueError:
    pass
else:
    raise TestFailed("if_indextoname() didn't raise ValueError")
