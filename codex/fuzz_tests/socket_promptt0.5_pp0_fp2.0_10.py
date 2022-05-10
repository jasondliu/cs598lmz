import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname != 'lo':
        raise Exception("Unexpected interface name: %r" % ifname)

# Test socket.if_nameindex()

def test_if_nameindex():
    interfaces = socket.if_nameindex()
    if len(interfaces) < 1:
        raise Exception("No interfaces found")

# Test socket.getaddrinfo()

def test_getaddrinfo():
    socket.getaddrinfo("localhost", None)

# Test socket.getnameinfo()

def test_getnameinfo():
    socket.getnameinfo(('127.0.0.1', 0, 0, 0), 0)

# Test socket.gethostbyname()

def test_gethostbyname():
    socket.gethostbyname("localhost")

# Test socket.gethostbyaddr()

def test_gethostbyaddr():
    socket.gethostbyaddr("127.0.0.1")

#
