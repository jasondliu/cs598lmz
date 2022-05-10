import socket
# Test socket.if_indextoname()
socket.if_indextoname(1)

# Test socket.inet_pton()
socket.inet_pton(socket.AF_INET, '127.0.0.1')
socket.inet_pton(socket.AF_INET6, '::1')

# Test socket.sendmsg()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendmsg(('127.0.0.1', 5555), (), (socket.SOL_SOCKET, socket.SCM_RIGHTS, b'12345'))
