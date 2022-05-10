import select
# Test select.select()

def test_select():
    import select
    import socket
    import time

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    s.listen(1)
    s.setblocking(0)

    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(s.getsockname())
    c.setblocking(0)

    sel = select.poll()
    sel.register(s, select.POLLIN)
    sel.register(c, select.POLLIN)

    # Wait for the connection to be accepted
    while 1:
        events = sel.poll()
        if events:
            break
        time.sleep(0.01)

    # Check that the connection is readable
    events = sel.poll()
    assert events == [(s.fileno(), select.POLLIN)]

    # Accept the connection
    conn, addr = s.accept()

