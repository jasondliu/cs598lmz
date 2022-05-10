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
    port = s.getsockname()[1]
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(('127.0.0.1', port))
    c.setblocking(0)
    s.accept()
    s.close()
    c.close()

    # test select() with an empty list
    for i in range(5):
        r, w, e = select.select([], [], [], 1.0)
        assert len(r) == len(w) == len(e) == 0

    # test select() with a zero timeout
    for i in range(5):
        r, w, e = select.select([], [], [], 0.
