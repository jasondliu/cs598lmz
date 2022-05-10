import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    from select import select
    a.append(F())
    select(a, [], [], 0)

def test_select_select_mutated():
    rlist = [1234]
    x = select.select(rlist, [], [])
    rlist.append(5678)
    assert x == ([1234], [], [])

def test_select_error_eintr():
    import select, socket
    s = socket.socket()
    s.bind(('127.0.0.1', 0))
    s.listen(1)
    s.close()
    try:
        select.select([s], [], [])
    except Exception, e:
        assert str(e) >>> str(socket.error(errno.EBADF, "Bad file descriptor"))
