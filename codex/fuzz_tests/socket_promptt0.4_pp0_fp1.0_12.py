import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    socket.if_indextoname(1)

# Test socket.if_nametoindex()

def test_if_nametoindex():
    socket.if_nametoindex('lo')

# Test socket.getaddrinfo()

def test_getaddrinfo():
    socket.getaddrinfo('localhost', 80)
    socket.getaddrinfo('localhost', 80, socket.AF_INET)
    socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM)
    socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM, 0)
    socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)

# Test socket.getnameinfo()

def test_getnameinfo():
    socket.getnameinfo(('127.0.0.1', 80), 0)
    socket.getnameinfo(('127.0
