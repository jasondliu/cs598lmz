import socket
# Test socket.if_indextoname()
if_indextoname = getattr(socket, 'if_indextoname', None)
if if_indextoname:
    try:
        if_indextoname(1)
    except ValueError:
        pass
    else:
        raise TestFailed("if_indextoname(1) didn't raise ValueError")
    try:
        if_indextoname(-1)
    except ValueError:
        pass
    else:
        raise TestFailed("if_indextoname(-1) didn't raise ValueError")
# Test socket.if_nameindex()
if_nameindex = getattr(socket, 'if_nameindex', None)
if if_nameindex:
    ni = if_nameindex()
    for i in ni:
        if i[0] < 0:
            raise TestFailed("if_nameindex returned an index < 0")
        if not isinstance(i[1], str):
            raise TestFailed("if_nameindex returned a non-string interface "
                             "name")
# Test socket.if
