import socket
socket.if_indextoname(2)

# 3.2.2.2.1.1
# 方法一：
import socket
socket.getaddrinfo('www.python.org', 'http')

# 方法二：
import socket
socket.getaddrinfo('www.python.org', 'http', 0, socket.SOCK_STREAM)

# 方法三：
import socket
socket.getaddrinfo('www.python.org', 'http', 0, socket.SOCK_STREAM, 0, socket.AI_ADDRCONFIG|socket.AI_V4MAPPED)

# 3.2.2.2.1.2
# 方法一：
import socket
socket.getnameinfo(('127.0.0.1', 8080), socket.NI_NUMERICHOST)

# 方法二：
import socket
