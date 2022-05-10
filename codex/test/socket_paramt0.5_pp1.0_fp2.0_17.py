import socket
socket.if_indextoname(3)

# Create a new socket using the given address family, socket type and protocol number.
# The address family should be AF_INET (the default), AF_INET6 or AF_UNIX.
# The socket type should be SOCK_STREAM (the default), SOCK_DGRAM or perhaps one of the other SOCK_ constants.
# The protocol number is usually zero and may be omitted in that case.
# socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
s = socket.socket()
print(s)

# Create a new socket using the given address family, socket type and protocol number.
# The address family should be AF_INET (the default), AF_INET6 or AF_UNIX.
# The socket type should be SOCK_STREAM (the default), SOCK_DGRAM or perhaps one of the other SOCK_ constants.
# The protocol number is usually zero and may be omitted in that case.
# socket.socket(family=AF_INET, type=SOCK_STREAM, proto=
