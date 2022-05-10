import socket
socket.if_indextoname(1)

# The if_indextoname() function takes an interface index as an argument and returns the corresponding interface name as a string.

# The if_nameindex() function returns a list of tuples. Each tuple contains an interface index and an interface name.

import socket
socket.if_nameindex()

# The if_nametoindex() function takes an interface name as an argument and returns the corresponding interface index as an integer.

import socket
socket.if_nametoindex('lo')

# The gethostbyname() function takes a hostname as an argument and returns the corresponding IPv4 address as a string.

import socket
socket.gethostbyname('localhost')

# The gethostbyname_ex() function takes a hostname as an argument and returns a tuple of three values: the canonical hostname, a list of aliases, and a list of IPv4 addresses.

import socket
socket.gethostbyname_ex('localhost')

# The gethostbyaddr() function takes an IPv4 address as an argument and returns a tuple of three values: the canonical hostname, a list of aliases, and a
