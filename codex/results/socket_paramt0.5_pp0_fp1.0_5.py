import socket
socket.if_indextoname(6)

# >>> socket.if_indextoname(6)
# 'en0'

# >>> socket.if_nametoindex('en0')
# 6

# >>> socket.gethostbyname('www.python.org')
# '82.94.164.162'

# >>> socket.gethostbyname_ex('www.python.org')
# ('www.python.org', [], ['82.94.164.162'])

# >>> socket.gethostbyaddr('82.94.164.162')
# ('www.python.org', [], ['82.94.164.162'])

# >>> socket.gethostname()
# 'pymotw.com'

# >>> socket.getfqdn()
# 'pymotw.com'

# >>> socket.getfqdn('82.94.164.162')
# 'www.python.org'

# >>> socket.getfqdn('82.94.164.162')
# 'www.python.org'

# >>> socket.getaddrinfo
