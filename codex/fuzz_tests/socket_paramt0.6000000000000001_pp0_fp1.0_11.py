import socket
socket.if_indextoname('3')

# If you want to do reverse lookups,
# use the socket.gethostbyaddr() function:

socket.gethostbyaddr('127.0.0.1')

# To find the fully qualified host name, use socket.getfqdn():

socket.getfqdn('127.0.0.1')

# To find out the IP address of the local machine, use socket.gethostbyname():

socket.gethostbyname(socket.gethostname())

# If you want to find the IP addresses of a remote host, use the
# socket.gethostbyname_ex() function:

socket.gethostbyname_ex('www.python.org')
