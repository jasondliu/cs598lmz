import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    from socket import if_indextoname
    if_indextoname(1)

# Test socket.if_nameindex()

def test_if_nameindex():
    from socket import if_nameindex
    if_nameindex()

# Test socket.if_nameindex()

def test_if_nameindex():
    from socket import if_nameindex
    if_nameindex()

# Test socket.if_nametoindex()

def test_if_nametoindex():
    from socket import if_nametoindex
    if_nametoindex('lo')

# Test socket.inet_aton()

def test_inet_aton():
    from socket import inet_aton
    inet_aton('127.0.0.1')

# Test socket.inet_ntoa()

def test_inet_ntoa():
    from socket import inet_ntoa
    inet_ntoa(b'\x7f\x00\x00\x01')

# Test socket
