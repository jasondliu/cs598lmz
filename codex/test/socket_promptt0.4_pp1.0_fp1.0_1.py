import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    print("Testing if_indextoname()")
    print(socket.if_indextoname(1))
    print(socket.if_indextoname(1, False))
    print(socket.if_indextoname(1, True))
    print(socket.if_indextoname(1, False, True))
    print(socket.if_indextoname(1, True, True))
    print(socket.if_indextoname(1, False, False))
    print(socket.if_indextoname(1, True, False))
    print(socket.if_indextoname(1, False, False, True))
    print(socket.if_indextoname(1, True, False, True))
    print(socket.if_indextoname(1, False, True, True))
    print(socket.if_indextoname(1, True, True, True))
