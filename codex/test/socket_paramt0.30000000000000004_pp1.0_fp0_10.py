import socket
socket.if_indextoname(3)

# 'en0'

# We can also do the reverse, going from a network interface name to an index:

socket.if_nametoindex('en0')

# 3

# These functions are useful when working with raw sockets, which we'll see in Chapter 12.

# Socket Addresses
# A socket address is the combination of an IP address and a port number, much like one end of a telephone connection is the combination of a phone number and a particular extension.
# 
# In most cases, IP addresses are assigned dynamically and port numbers are assigned by the application that will be using the connection. However, it is sometimes useful to be able to specify a port number in advance.
# 
# For example, the port number for the FTP service is 21, so if you are setting up a publicly accessible FTP server, you may want to bind the server to the address 192.168.1.100 and port 21.
# 
# The socket module defines a number of functions that are used to convert between human-readable addresses and the packed binary format used in low-level network functions.
# 
# For example, the function socket.
