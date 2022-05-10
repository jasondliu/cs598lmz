import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    if_indextoname = socket.if_indextoname
    try:
        if_indextoname(1)
    except OSError as e:
        if e.errno != errno.ENXIO:
            raise
    else:
        raise Exception("if_indextoname(1) should have raised ENXIO")
    try:
        if_indextoname(0)
    except OSError as e:
        if e.errno != errno.ENXIO:
            raise
    else:
        raise Exception("if_indextoname(0) should have raised ENXIO")
    try:
        if_indextoname(-1)
    except OSError as e:
        if e.errno != errno.ENXIO:
            raise
    else:
        raise Exception("if_indextoname(-1) should have raised ENXIO")
    try:
        if_indext
