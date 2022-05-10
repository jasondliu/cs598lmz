import socket
# Test socket.if_indextoname()

# This test is not very thorough, but it does check that
# the function returns a string and that the string is
# not empty.

print(socket.if_indextoname(1))
