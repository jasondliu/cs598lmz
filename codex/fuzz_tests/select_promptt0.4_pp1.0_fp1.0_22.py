import select
# Test select.select()

def test_select():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    s.listen(1)
    s.setblocking(0)
    conn, addr = s.accept()
    conn.setblocking(0)
    print select.select([s], [], [], 0.1)
    print select.select([conn], [], [], 0.1)
    print select.select([s, conn], [], [], 0.1)
    conn.close()
    s.close()

# test_select()

# Test that select.select() raises an error if the file descriptor is too large.
# (On some platforms, it may return success instead.)

def test_large_fd():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    s.listen(1
