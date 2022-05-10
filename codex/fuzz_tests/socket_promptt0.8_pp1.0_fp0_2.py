import socket
# Test socket.if_indextoname
if socket.if_indextoname(0):
    print('if_indextoname() supported')
else:
    print('if_indextoname() not supported')


# Test socket.if_nameindex
if socket.if_nameindex():
    print('if_nameindex() supported')
else:
    print('if_nameindex() not supported')


# Test socket.getaddrinfo
try:
    socket.getaddrinfo('localhost', 80)
    print('getaddrinfo() supported')
except Exception:
    print('getaddrinfo() not supported')


# Test socket.getnameinfo
try:
    socket.getnameinfo(('127.0.0.1', 80), 0)
    print('getnameinfo() supported')
except Exception:
    print('getnameinfo() not supported')


# Test socket.getfqdn
try:
    socket.getfqdn('127.0.0.1')
    print('getfqdn() supported')
except Exception:
    print('getfqdn() not supported')


#
