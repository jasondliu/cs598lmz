import socket
# Test socket.if_indextoname()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    names = [socket.if_indextoname(i) for i in range(socket.if_nametoindex(''))]
    assert isinstance(names, list)
    assert socket.if_indextoname(0) == ''
    assert socket.if_indextoname(socket.if_nametoindex('lo')) == 'lo'
    #
    try:
        socket.if_indextoname(-1)
    except ValueError:
        pass
    else:
        print('socket.if_indextoname(-1) expected raise ValueError')
    try:
        socket.if_indextoname(1 << 32)
    except ValueError:
        pass
    else:
        print('socket.if_indextoname(1 << 32)) expected raise ValueError')
    try:
        socket.if_indextoname(socket.if_nametoindex('lo') + 1)
    except ValueError:
        pass

