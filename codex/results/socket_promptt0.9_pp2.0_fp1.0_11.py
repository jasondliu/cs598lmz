import socket
# Test socket.if_indextoname and socket.if_nametoindex.
# These are supported on Windows, Linux and OSX.
assert socket.if_indextoname(1) == 'lo0'
assert socket.if_nametoindex('lo0') == 1
