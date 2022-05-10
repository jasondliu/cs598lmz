import socket
# Test socket.if_indextoname() function

if_indextoname = socket.if_indextoname

# Check if the function raises an exception when asked to convert an invalid
# index.
try:
    if_indextoname(0)
except OSError:
    pass
else:
    print("if_indextoname(0) should have failed")

# Check if the function raises an exception when asked to convert an invalid
# index.
try:
    if_indextoname(99999)
except OSError:
    pass
else:
    print("if_indextoname(99999) should have failed")
