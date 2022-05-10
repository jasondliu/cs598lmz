import socket
socket.if_indextoname(3)

# get interface name
socket.gethostname()

# get ip address
socket.gethostbyname(socket.gethostname())

# get hostname
socket.getfqdn()

# get ip address
socket.gethostbyname(socket.getfqdn())

# get ip address
socket.gethostbyname_ex(socket.getfqdn())[2][0]

# get hostname
socket.gethostbyaddr('192.168.0.1')

# get ip address
socket.gethostbyname_ex('www.google.com')[2][0]

# get ip address
socket.gethostbyname_ex('www.google.com')[2]

# get ip address
socket.gethostbyname_ex('www.google.com')[2][1]

# get ip address
socket.gethostbyname_ex('www.google.com')[2][2]

# get ip address
socket.gethostbyname_ex('www.google.com')[2][3]


