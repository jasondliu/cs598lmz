import socket
# Test socket.if_indextoname() with nonexistent if index
def test_if_indextoname(dev, apdev):
    """socket.if_indextoname() with nonexistent if index"""
    try:
        socket.if_indextoname(9999999)
        raise Exception("if_indextoname() succeeded unexpectedly")
    except socket.error as e:
        if e.errno != errno.EINVAL:
            raise

@remote_compatible
def test_getaddrinfo(dev, apdev):
    """socket.getaddrinfo()"""
    res = socket.getaddrinfo(apdev[0]['ifname'], None)
    if len(res) < 1:
        raise Exception("Could not get address info")
    res = socket.getaddrinfo(apdev[0]['ifname'], None, socket.AF_INET)
    if len(res) < 1:
        raise Exception("Could not get address info (AF_INET)")
    res = socket.getaddrinfo(apdev[0]['ifname'], None, 0, socket.SOCK_
