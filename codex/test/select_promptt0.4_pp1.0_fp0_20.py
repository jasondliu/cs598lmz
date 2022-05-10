import select
# Test select.select

def test_select():
    """
    >>> test_select()
    """
    import socket
    import sys
    import time
    import select

    # create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # associate the socket to host and port
    s.bind(("localhost", 0))

    # listenning
    s.listen(5)

    # get the port
    port = s.getsockname()[1]

    # create clients and connect to the server
    clients = []
    for res in socket.getaddrinfo("localhost",
                                  port,
                                  socket.AF_UNSPEC,
                                  socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            s = None
            continue
        try:
            s.connect(sa)
        except socket.error as msg:
            s.close()
