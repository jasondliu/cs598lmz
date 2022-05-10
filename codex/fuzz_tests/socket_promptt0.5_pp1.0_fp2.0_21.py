import socket
# Test socket.if_indextoname()
from socket import if_indextoname

def test_if_indextoname():
    index = socket.if_nametoindex('lo')
    name = socket.if_indextoname(index)
    assert name == 'lo'
    assert type(name) is str

# Test socket.if_nameindex()
from socket import if_nameindex

def test_if_nameindex():
    nics = socket.if_nameindex()
    assert type(nics) is list
    assert len(nics) > 0
    assert type(nics[0]) is tuple
    assert len(nics[0]) == 2
    assert type(nics[0][0]) is int
    assert type(nics[0][1]) is str

# Test socket.if_nametoindex()
from socket import if_nametoindex

def test_if_nametoindex():
    index = socket.if_nametoindex('lo')
    assert type(index) is int

# Test socket.getaddrinfo()
from socket import getaddrinfo

