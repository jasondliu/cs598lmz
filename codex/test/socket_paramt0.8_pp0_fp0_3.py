import socket
socket.if_indextoname(3)

'lo0'

socket.if_nameindex()

[(1, 'lo0'), (2, 'gif0'), (3, 'stf0')]

socket.if_nametoindex('en0')

2

socket.gethostbyaddr('127.0.0.1')

('localhost', [], ['127.0.0.1'])

socket.gethostbyname('www.python.org')

'82.94.164.162'

socket.gethostname()

'paulbookpro.local'

socket.gethostbyname_ex('www.python.org')

('82.94.164.162', [], ['82.94.164.162'])

time.gmtime(0)

