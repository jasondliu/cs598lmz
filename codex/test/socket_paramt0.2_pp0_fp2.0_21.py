import socket
socket.if_indextoname(3)

# 'en0'

socket.if_nametoindex('en0')

# 3

socket.gethostbyname('www.python.org')

# '82.94.164.162'

socket.gethostbyname_ex('www.python.org')

# ('www.python.org', [], ['82.94.164.162'])

socket.gethostbyaddr('82.94.164.162')

# ('www.python.org', [], ['82.94.164.162'])

socket.gethostname()

# 'pilgrim-mbp.home'

socket.getfqdn()

# 'pilgrim-mbp.home'

socket.getaddrinfo('www.python.org', 'http')

# [(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('82.94.164.162', 80)), (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_DGRAM:
