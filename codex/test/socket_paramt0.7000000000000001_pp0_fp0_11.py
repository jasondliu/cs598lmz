import socket
socket.if_indextoname('0')

my_ip = socket.gethostbyname(socket.gethostname())
