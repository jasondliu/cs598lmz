import socket
socket.if_indextoname(3)

# socket.if_nameindex()
socket.if_nametoindex('lo')

# socket.getservbyname()
socket.getservbyname('http','tcp')

# socket.getservbyport()
socket.getservbyport(21)

# socket.htons()
socket.htons(21)

# socket.ntohs()
socket.ntohs(1234)

# socket.inet_aton()
socket.inet_aton("127.0.0.1")

# socket.inet_ntoa()
socket.inet_ntoa("127.0.0.1")

# socket.inet_pton()
socket.inet_pton(socket.AF_INET,"127.0.0.1")

# socket.inet_ntop()
socket.inet_ntop(socket.AF_INET,"127.0.0.1")

# socket.getsockopt()
socket.getsockopt(s,socket.SOL_SOCKET,socket.SO_TYPE)

# socket.setsock
