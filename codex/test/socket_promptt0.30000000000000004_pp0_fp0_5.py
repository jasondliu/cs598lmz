import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    print(socket.if_indextoname(1))

def test_if_nameindex():
    print(socket.if_nameindex())

def test_if_nametoindex():
    print(socket.if_nametoindex('lo'))

def test_gethostbyname():
    print(socket.gethostbyname('www.baidu.com'))

def test_gethostbyname_ex():
    print(socket.gethostbyname_ex('www.baidu.com'))

def test_gethostbyaddr():
    print(socket.gethostbyaddr('127.0.0.1'))

def test_gethostname():
    print(socket.gethostname())

def test_getfqdn():
    print(socket.getfqdn())

def test_getaddrinfo():
    print(socket.getaddrinfo('www.baidu.com', 80))

