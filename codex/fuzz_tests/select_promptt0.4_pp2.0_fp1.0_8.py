import select
# Test select.select

def test_select():
    import select
    import socket

    # Some platforms (e.g. OSF1) don't support select on pipes.
    # Also, Windows doesn't support select on pipes.
    if hasattr(select, 'PIPE_BUF'):
        # Create a pair of connected sockets
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.bind(('localhost', 0))
        lsock.listen(1)
        addr, port = lsock.getsockname()
        csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        csock.connect(('localhost', port))

        # Create another pair of connected sockets
        lsock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock2.bind(('localhost', 0))
        lsock2.listen(1)
        addr, port = lsock2.getsockname()
        csock2 = socket.socket(socket.AF
