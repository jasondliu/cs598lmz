import socket
socket.if_indextoname(3)

# 'en0'

socket.if_nametoindex('en0')

# 3

socket.gethostbyname('localhost')

# '127.0.0.1'

socket.gethostbyname_ex('localhost')

# ('localhost', [], ['127.0.0.1'])

socket.gethostbyaddr('127.0.0.1')

# ('localhost', [], ['127.0.0.1'])

socket.gethostname()

# 'macbook-pro.local'

socket.gethostbyname_ex(socket.gethostname())

# ('macbook-pro.local', [], ['127.0.0.1'])

socket.gethostbyaddr(socket.gethostbyname(socket.gethostname()))

# ('macbook-pro.local', [], ['127.0.0.1'])

socket.getfqdn()

# 'macbook-pro.local'

