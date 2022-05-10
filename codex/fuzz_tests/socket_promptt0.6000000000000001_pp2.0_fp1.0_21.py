import socket
# Test socket.if_indextoname()
try:
    socket.if_indextoname(1)
except:
    print('SKIP')
    sys.exit()

import uos

# Test getaddrinfo
print(socket.getaddrinfo('localhost', 80))
print(socket.getaddrinfo('localhost', 80, socket.AF_INET))
print(socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM))

# Test getnameinfo
print(socket.getnameinfo(('127.0.0.1', 80)))
print(socket.getnameinfo(('127.0.0.1', 80), socket.AI_CANONNAME))
print(socket.getnameinfo(('127.0.0.1', 80), 0))

# Test gethostbyname
print(socket.gethostbyname('localhost'))

# Test gethostbyname_ex
print(socket.gethostbyname_ex('localhost'))

# Test gethostbyaddr
print(socket.gethostbyaddr('127.0.0.1'
