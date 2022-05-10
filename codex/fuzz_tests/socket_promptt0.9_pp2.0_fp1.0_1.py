import socket
# Test socket.if_indextoname

# These have to match the test devices
try:
    if_nametoindex = socket.if_nametoindex
    if_indextoname = socket.if_indextoname
except AttributeError:
    pass
else:
    # Verify that a device can be found
    index = if_nametoindex('lo')
    name = if_indextoname(index)
    assert name == 'lo'
