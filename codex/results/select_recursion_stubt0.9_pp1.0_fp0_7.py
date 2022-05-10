import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated().append(1)

    select.select([],[F()],[])
    assert a == [1]

def test_poll_methods():
    p = select.poll()
    p.register(1)
    p.unregister(1)

def test_poll_wait():
    p = select.poll()
    p.register(10)
    p.poll(0)
    py.test.raises(select.error, p.poll, -1)

def test_register():
    p = select.poll()
    p.register(10)

def test_modify():
    p = select.poll()
    p.register(10, select.POLLIN)
    p.modify(10, select.POLLOUT)

def test_select():
    a = []
    b = []

    class F:
        def fileno(self):
            a.append(1)

    class G: pass

    select.select([F()], [F(), G()], [F(), G()])
    assert a == [1, 1, 1
