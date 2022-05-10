import socket
socket.if_indextoname('6')

# 'en0'

socket.if_indextoname(6)

# 'en0'

socket.if_nametoindex('en1')

# 7
socket.if_nametoindex('p2p0')

# 19

socket.gethostbyname('localhost')

# '127.0.0.1'

socket.gethostbyname_ex('localhost')

# ('localhost', [], ['127.0.0.1'])

socket.gethostbyname('www.python.org')

# '151.101.64.223'

socket.gethostbyname_ex('www.python.org')

# ('www.python.org', [], ['151.101.64.223'])

socket.gethostname()

# 'Jackson-MBP.local'

socket.getfqdn()

# 'Jackson-MBP.local'
socket.getfqdn('localhost')

# 'localhost'

socket.getfqdn('127.0.0.1
