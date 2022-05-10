import socket
socket.if_indextoname(3)

# socket.if_nameindex()
# Return a list of network interface information.
# Each element of the list is a tuple containing a string giving the name of the interface and an integer giving the corresponding index.
socket.if_nameindex()

# socket.if_nametoindex(if_name)
# Return the index of the interface if_name.
socket.if_nametoindex('en0')

# socket.gethostbyname(hostname)
# Return the IP address (a string of the form '255.255.255.255') for a host.
socket.gethostbyname('www.google.com')

# socket.gethostbyname_ex(hostname)
# Return the true host name, a list of aliases, and a list of IP addresses, for a host.
socket.gethostbyname_ex('www.google.com')

# socket.gethostname()
# Return a string containing the hostname of the machine where the Python interpreter is currently executing.
socket.gethostname()

# socket.gethostbyaddr(ip_address)
#
