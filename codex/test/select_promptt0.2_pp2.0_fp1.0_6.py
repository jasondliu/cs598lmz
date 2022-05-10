import select
# Test select.select()

def test_select():
    import select
    import socket
    import time

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 0))
    server.listen(5)
    port = server.getsockname()[1]

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', port))

    r, w, x = select.select([client], [], [], 1.0)
    assert r == []
    assert w == []
    assert x == []

    server.accept()

    r, w, x = select.select([client], [], [], 1.0)
    assert r == [client]
    assert w == []
    assert x == []

    client.close()
    server.close()

def test_select_timeout():
    import select
    import socket
    import time

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

