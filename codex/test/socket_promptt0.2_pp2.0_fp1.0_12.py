import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    for i in range(100):
        try:
            socket.if_indextoname(i)
        except ValueError:
            pass
        else:
            assert socket.if_indextoname(i)

# Test socket.if_nameindex()

def test_if_nameindex():
    for i in socket.if_nameindex():
        assert socket.if_indextoname(i[0]) == i[1]

# Test socket.if_nametoindex()

def test_if_nametoindex():
    for i in socket.if_nameindex():
        assert socket.if_nametoindex(i[1]) == i[0]

# Test socket.gethostbyname_ex()

def test_gethostbyname_ex():
    for name in ('localhost', 'www.python.org', 'www.google.com'):
        (name, aliaslist, ipaddrlist) = socket.gethostbyname_ex(name)
        assert name in aliaslist

