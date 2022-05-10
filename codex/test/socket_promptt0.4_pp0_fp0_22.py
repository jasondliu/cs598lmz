import socket
# Test socket.if_indextoname()

def test_if_indextoname(name):
    print(socket.if_indextoname(socket.if_nametoindex(name)))

def test_if_indextoname_exception():
    try:
        socket.if_indextoname(0)
    except socket.error as e:
        print(e)

def test_if_indextoname_exception2():
    try:
        socket.if_indextoname(1000000)
    except socket.error as e:
        print(e)

def test_if_indextoname_exception3():
    try:
        socket.if_indextoname(0.1)
    except TypeError as e:
        print(e)

def test_if_indextoname_exception4():
    try:
        socket.if_indextoname('abc')
    except TypeError as e:
        print(e)

