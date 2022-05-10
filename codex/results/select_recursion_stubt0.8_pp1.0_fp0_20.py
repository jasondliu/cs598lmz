import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(None)
            return 0

    select.select([F()], [], [], 1)
    check(a)

def test_select_del():
    a = []

    class F:
        def fileno(self):
            a.append(None)
            return 0

    f = F()
    select.select([f], [], [], 1)
    del f
    assert not a
