import socket
socket.if_indextoname(2)

'lo'

socket.if_nameindex()

[(1, 'lo'), (2, 'eth0'), (3, 'wlan0')]

socket.gethostbyname('localhost')

'127.0.0.1'

socket.gethostbyname_ex('localhost')

('localhost', [], ['127.0.0.1'])

socket.gethostbyaddr('127.0.0.1')

('localhost', [], ['127.0.0.1'])

socket.getservbyname('http')

80

socket.getservbyport(80)

'http'

socket.getprotobyname('icmp')

1

socket.getprotobyname('tcp')

6

socket.getaddrinfo('www.python.org', 'http')

[(2, 1, 0, '', ('82.94.164.162', 80))]

