import socket
socket.if_indextoname(0)

# socket.inet_ntoa(bytes)
# socket.inet_ntoa(bytes('\x7f\x00\x00\x01', 'utf-8'))

# socket.gethostbyname(host)
# socket.gethostbyname('www.python.org')

# socket.gethostbyaddr(ip)
# socket.gethostbyaddr('127.0.0.1')

# socket.gethostname()

# socket.getaddrinfo(host, port, family, type, proto, flags)
'''
socket.getaddrinfo('www.python.org', 'http')
[(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('82.94.164.162', 80)), (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_DGRAM: 2>, 17, '', ('82.94.164.162', 80)), (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_RAW: 3>, 0, '
