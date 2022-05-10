import socket
# Test socket.if_indextoname
#
# Copyright (C) 2018, Guillaume Gonnet
# This project is under the MIT License

# Get an interface name from its index
if_name = socket.if_indextoname(1)
assert if_name == "lo", if_name

# Get an interface name from an invalid index
try:
    socket.if_indextoname(65536)
except ValueError:
    pass
else:
    raise AssertionError("An exception should have been raised.")

# Get an interface name from an invalid index
try:
    socket.if_indextoname(-1)
except ValueError:
    pass
