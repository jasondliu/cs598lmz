import socket
# Test socket.if_indextoname()

def test_socket_if_indextoname():
    """
    Test socket.if_indextoname()
    """
    if_indextoname = socket.if_indextoname
    if_indextoname(1)

def test_socket_if_nameindex():
    """
    Test socket.if_nameindex()
    """
    if_nameindex = socket.if_nameindex
    if_nameindex()

def test_socket_if_nametoindex():
    """
    Test socket.if_nametoindex()
    """
    if_nametoindex = socket.if_nametoindex
    if_nametoindex("lo")

def test_socket_gethostbyaddr():
    """
    Test socket.gethostbyaddr()
    """
    gethostbyaddr = socket.gethostbyaddr
    gethostbyaddr("127.0.0.1")

def test_socket_gethostbyname():
    """
    Test socket.gethostbyname()
    """
    gethostbyname =
