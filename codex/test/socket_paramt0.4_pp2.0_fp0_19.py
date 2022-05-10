import socket
socket.if_indextoname(2)

# get the ip address of the interface
socket.if_nameindex()

# get the ip address of the interface
socket.if_nametoindex('eth0')

# get the ip address of the interface
socket.gethostbyname('google.com')

# get the ip address of the interface
socket.gethostbyname_ex('google.com')

# get the ip address of the interface
socket.gethostbyaddr('127.0.0.1')

# get the ip address of the interface
socket.gethostname()

# get the ip address of the interface
socket.gethostbyname_ex(socket.gethostname())[2]

# get the ip address of the interface
socket.gethostbyname_ex(socket.gethostname())[2][0]

# get the ip address of the interface
socket.gethostbyname_ex(socket.gethostname())[2][1]

# get the ip address of the interface
socket.gethostbyname_ex(socket.gethostname())[2][2]


