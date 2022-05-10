import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    if_indextoname = socket.if_indextoname
    try:
        if_indextoname(0)
    except OSError as e:
        if e.errno == errno.EINVAL:
            print("skipped")
            return
        raise
    print("if_indextoname(0) =", if_indextoname(0))

test_if_indextoname()
