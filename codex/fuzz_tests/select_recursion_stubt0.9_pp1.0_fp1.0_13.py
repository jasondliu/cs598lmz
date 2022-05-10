import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            del a[:]
            return 15

    class F2:
        def fileno(self):
            assert False

    f = F()
    f2 = F2()

    def wakeup():
        a.append(f2)
        yield

    trampoline(wakeup())
    for i in range(4):
        a.append(f)
        select.select([f, f2], [], [])
    py.test.raises(IndexError, select.select, [f], [], [])
