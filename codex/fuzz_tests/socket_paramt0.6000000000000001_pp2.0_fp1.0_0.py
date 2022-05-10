import socket
socket.if_indextoname(1)

socket.inet_ntop(socket.AF_INET, socket.inet_pton(socket.AF_INET, '127.0.0.1'))

socket.gethostname()
socket.gethostbyname(socket.gethostname())

socket.getservbyname('http')
socket.getservbyport(80)

socket.getaddrinfo('www.google.com', 80, socket.AF_INET, socket.SOCK_STREAM)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 0))
s.getsockname()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 0))
s.listen(1)
s.getsockname()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.google.com', 80))
s.
