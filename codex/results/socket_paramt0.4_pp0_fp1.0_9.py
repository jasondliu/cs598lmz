import socket
socket.if_indextoname(1)

# If you want to get the name of the interface for a given IP address, use the
# gethostbyaddr() function.
print socket.gethostbyaddr('127.0.0.1')

# If you want to get the IP address for a given hostname, use the gethostbyname()
# function.
print socket.gethostbyname('localhost')

# If you want to get all the IP addresses for a given hostname, use the
# gethostbyname_ex() function.
print socket.gethostbyname_ex('localhost')

# If you want to get the IP address for a given hostname and port, use the
# gethostbyname() function.
print socket.gethostbyname_ex('localhost', 80)

# If you want to get the fully qualified domain name for a given IP address, use
# the getfqdn() function.
print socket.getfqdn('127.0.0.1')

# If you want to get the fully qualified domain name for the local machine, use
# the getfqdn() function.
print
