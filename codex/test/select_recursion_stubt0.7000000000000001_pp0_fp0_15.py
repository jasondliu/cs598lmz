import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    assert select.select([F()], [], [], 0) == ([], [], [])
    raises(IndexError, select.select, [F()], [], [], 0)

def test_bad_fd():
    import socket
    s = socket.socket()
    s.close()
    raises(select.error, "select.select([s], [], [], 0)", globals(), locals())

def test_big_fd():
    import socket
    s = socket.socket()
    s.close()
    fd = 110000
    while fd > s.fileno():
        os.dup(s.fileno())
        fd -= 1
    try:
        raises(select.error, "select.select([s], [], [], 0)", globals(), locals())
    finally:
        for fd in range(s.fileno() + 1, 110000):
            os.close(fd)

def test_select_returns_None_when_interrupted():
    import errno
    import select
   
