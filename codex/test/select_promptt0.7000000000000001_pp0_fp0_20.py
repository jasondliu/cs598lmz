import select
# Test select.select()

def test_select():
    # Note:
    #    This test only works for TCP connections; a UDP socket
    #    will not respond to select() in the same way.  (There
    #    are no known UDP sockets that support select().)
    import socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 0))
    server.listen(5)
    port = server.getsockname()[1]
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', port))
    r, w, e = select.select([client], [], [])
