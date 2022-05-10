import socket
socket.if_indextoname(3)

# get interfaces
socket.if_nameindex()
 
# get IP address
socket.gethostbyaddr('192.168.1.1')

# get hostname
socket.gethostname()

# get hostname
socket.getfqdn()

# get hostname
socket.gethostbyname('localhost')

# get hostname
socket.gethostbyname_ex('localhost')

# get hostname
socket.gethostbyname_ex('localhost')[2]

# get hostname
socket.gethostbyaddr('127.0.0.1')

# get hostname
socket.gethostbyaddr('127.0.0.1')[0]

# get hostname
socket.gethostbyaddr('127.0.0.1')[2]

# get hostname
socket.gethostbyaddr('127.0.0.1')[2][0]

# get hostname
socket.gethostbyaddr('127.0.0.1')[2][3]

# get hostname
