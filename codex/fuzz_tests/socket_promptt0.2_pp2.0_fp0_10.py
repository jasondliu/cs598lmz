import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    if_indextoname = socket.if_indextoname
    try:
        if_indextoname(1)
    except OSError as err:
        if err.errno != errno.ENXIO:
            raise
    else:
        raise Exception('Expected OSError')

test_if_indextoname()
