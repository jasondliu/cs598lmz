import select
# Test select.select
def test_select():
    import select
    import socket
    import time
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 5000))
    server.listen(1)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5000))
    client.send(b'hello')
    r, w, x = select.select([server], [], [], 0)
    assert r == [server]
    client.close()
    server.close()
    time.sleep(0.1)
    r, w, x = select.select([server], [], [], 0)
    assert r == []

# Test select.poll
def test_poll():
    import select
    import socket
    import time
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 5000))
    server.listen(1)
