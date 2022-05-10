import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def fd_closed(self):
            assert 0

        def fd_may_recv(self):
            a.append(self)

    class T:
        def fileno(self):
            return 1

        def fd_closed(self):
            assert 0

        def fd_may_recv(self):
            assert 0

    f1 = F()
    t = T()

    select.select([f1], [], [], 0)
    assert a == [f1]
    del a[:]

    select.select([f1, t], [], [], 0)
    assert a == [f1]
    del a[:]
