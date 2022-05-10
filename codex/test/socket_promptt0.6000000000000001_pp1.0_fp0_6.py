import socket
# Test socket.if_indextoname(), socket.if_nameindex(), socket.if_nametoindex()

def test_if_nameindex():
    if_nameindex = socket.if_nameindex
    # test that we can call it
    if_nameindex()

def test_if_nametoindex():
    if_nametoindex = socket.if_nametoindex
    # test that we can call it
    if_nametoindex('lo')

def test_if_indextoname():
    if_indextoname = socket.if_indextoname
    # test that we can call it
    if_indextoname(1)
