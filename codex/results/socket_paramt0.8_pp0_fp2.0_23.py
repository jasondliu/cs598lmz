import socket
socket.if_indextoname('18')

#Get if_name
socket.if_nameindex()

#Get if_names
socket.if_names

#Get IP address from name
socket.gethostbyname('localhost')

#Get IP address from name
socket.gethostbyaddr('127.0.0.1')

#Get IP address from hostname
socket.gethostbyname_ex('localhost')

#Get hostname infos
socket.gethostname()

#Get all IP addresses
socket.getaddrinfo('localhost',80)

#Get the FQDN
socket.getfqdn('localhost')

#Get the name of the host
socket.gethostname()
