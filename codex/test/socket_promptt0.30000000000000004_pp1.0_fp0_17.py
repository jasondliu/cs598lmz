import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    """
    Test socket.if_indextoname()
    """
    # Test if_indextoname()
    if_indextoname = socket.if_indextoname
    # Test if_indextoname() with invalid index
    try:
        if_indextoname(0)
    except OSError as e:
        if e.errno != errno.EINVAL:
            raise
    else:
        raise Exception('Expected OSError')
    # Test if_indextoname() with valid index
    try:
        if_indextoname(1)
    except OSError:
        raise Exception('Unexpected OSError')

if __name__ == '__main__':
    test_if_indextoname()
