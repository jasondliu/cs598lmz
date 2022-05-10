import socket
# Test socket.if_indextoname()

def if_indextoname(index):
    try:
        return socket.if_indextoname(index)
    except OverflowError:
        return socket.if_indextoname(int(index))

def test_if_indextoname():
    if not hasattr(socket, 'if_indextoname'):
        return
    print(if_indextoname(1))
    print(if_indextoname(1000))
    print(if_indextoname(0))
    try:
        print(if_indextoname(-1))
    except ValueError as msg:
        print(msg)
    print(if_indextoname(2**32+1))

test_if_indextoname()
