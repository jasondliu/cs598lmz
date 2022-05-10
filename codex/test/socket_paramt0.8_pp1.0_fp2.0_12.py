import socket
socket.if_indextoname(3)
#'en0'


socket.getprotobyname('tcp')
# 6

socket.getservbyname('http','tcp')
#80

socket.getaddrinfo('www.python.org','http')
#[(2, 1, 6, '', ('82.94.164.162', 80)), (2, 2, 17, '', ('82.94.164.162', 80)), (30, 1, 6, '', ('2001:888:2000:d::a2', 80, 0, 0)), (30, 2, 17, '', ('2001:888:2000:d::a2', 80, 0, 0))]
