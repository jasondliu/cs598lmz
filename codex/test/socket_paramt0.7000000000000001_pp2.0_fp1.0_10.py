import socket
socket.if_indextoname(1)
'eth0'
socket.if_nameindex()
[(1, 'eth0'), (2, 'lo')]
socket.if_nameindex()[0][1]
'eth0'
socket.if_indextoname(1)
'eth0'
socket.gethostname()
'evgeny-ubuntu'
socket.gethostbyname('localhost')
'127.0.0.1'
socket.gethostbyname('evgeny-ubuntu')
'192.168.1.121'
socket.gethostbyaddr('192.168.1.121')
('evgeny-ubuntu', [], ['192.168.1.121'])
socket.gethostbyaddr('192.168.1.121')[0]
'evgeny-ubuntu'
socket.gethostbyaddr('192.168.1.121')[2]
['192.168.1.121']
socket.gethostbyaddr('192.168.1.121')[2][0]
'192.168.1.121'
socket.getdefaulttimeout()
