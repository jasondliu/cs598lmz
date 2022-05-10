import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    select.select([F()], a, a)

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.append(1)

    select.select([F()], a, a)
    assert a == [1], a

def test_register_readwrite():
    r = select.poll()
    w = select.poll()
    r.register(0, select.POLLIN)
    w.register(0, select.POLLOUT)

def test_register_with_fd():
    p = select.poll()
    os_fd = os.open(__file__, os.O_RDONLY)
    try:
        p.register(os_fd, select.POLLIN)
        r = p.poll(1)
        assert r == [(os_fd, select.POLLIN)], r
    finally:
        os.close(os_fd)

def test_register_bad_fd():
    p = select.poll()
