import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    if_indextoname = socket.if_indextoname
    try:
        if_indextoname(0)
    except OSError:
        pass
    else:
        print('if_indextoname(0) should have failed')
    try:
        if_indextoname(-1)
    except OSError:
        pass
    else:
        print('if_indextoname(-1) should have failed')
    try:
        if_indextoname(1<<32)
    except OSError:
        pass
    else:
        print('if_indextoname(1<<32) should have failed')
    try:
        if_indextoname(1<<128)
    except OverflowError:
        pass
    else:
        print('if_indextoname(1<<128) should have failed')
    try:
        if_indextoname(1.5)
    except TypeError:
        pass
