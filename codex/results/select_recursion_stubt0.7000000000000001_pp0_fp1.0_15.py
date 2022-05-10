import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    f = F()
    select.select([f], [], [], -1)

def test_select_error():
    import errno
    try:
        select.select([], [], [], 0)
    except select.error as e:
        if e.args[0] != errno.EINTR:
            raise
    else:
        raise RuntimeError("Exception not raised")

def test_select_poll():
    import socket
    import errno

    a, b = socket.socketpair()
    a.send(b"1")
    try:
        select.poll().register(a)
    except select.error as e:
        if e.args[0] != errno.EINVAL:
            raise
    else:
        raise RuntimeError("Exception not raised")
    a.close()
    b.close()

def test_select_poll_unregister():
    import socket

    a, b = socket.socketpair()
    p = select.poll()
    p.register(a)

