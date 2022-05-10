import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    f = F()
    select.select([f], [], [])

def test_select_poll():
    a = select.poll()
    b = select.poll()
    c = select.poll()
    c.poll()
    d = select.poll()
    for i in range(5):
        a.register(i, select.POLLIN|select.POLLOUT)
        b.register(i, select.POLLIN|select.POLLOUT)
    newfds = {}
    a.poll()
    b.poll()
    c.poll()
    d.poll()
    for i in (-1, 5):
        newfds[i] = select.POLLIN
    a.register(1, select.POLLIN|select.POLLOUT)
    b.modify(1, select.POLLIN|select.POLLOUT)
    a.register(2, select.POLLIN|select.POLLOUT)
    b.modify(2, select.POLLIN|select.PO
