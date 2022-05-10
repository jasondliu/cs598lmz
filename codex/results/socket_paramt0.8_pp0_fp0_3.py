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

time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_
