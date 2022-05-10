import socket
socket.if_indextoname(3)

# get the interface name of the interface with index 3
socket.if_nameindex()

# get the index and name of all the interfaces
socket.if_nametoindex('lo')

# get the index of the interface with name 'lo'
socket.gethostbyname('www.google.com')

# get the IP address of the host with name 'www.google.com'
socket.gethostbyname_ex('www.google.com')

# get the IP address of the host with name 'www.google.com'
socket.gethostbyaddr('216.58.211.100')

# get the host name of the host with IP address '216.58.211.100'
socket.gethostname()

# get the host name of the current machine
socket.gethostbyname_ex(socket.gethostname())

# get the IP address of the current machine
socket.getfqdn()

# get the fully qualified domain name of the current machine
socket.getaddrinfo('www.google.com', 80)

# get the IP address and
