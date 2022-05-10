import socket
socket.if_indextoname(3)

# socket.if_nameindex()
# Return a list of network interface information.
# Each element of the list is a tuple that contains
# the interface name and the corresponding index.
socket.if_nameindex()

# socket.if_nameinfo(sockaddr, flags)
# Translate a socket address sockaddr into a 2-tuple
# (host, port). Depending on the settings of flags,
# the result can contain a fully-qualified domain name
# or numeric address representation in host.
# Similarly, port can contain a string port name or a
# numeric port number.
socket.if_nameinfo(('192.168.0.1', 80))

# socket.socketpair([family[, type[, proto]]])
# Create a pair of connected socket objects using the
# given address family, socket type, and protocol number.
# The default family is AF_UNIX if defined on the platform;
# otherwise, the default is AF_INET.
# The default type is SOCK_STREAM.
# The default protocol is 0.
