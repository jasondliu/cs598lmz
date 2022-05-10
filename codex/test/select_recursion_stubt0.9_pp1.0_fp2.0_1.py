import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
        def foobar(self):
            del a[:]
    a.append(F())

    try:
        select.select([a[0]], [], [])
        assert False, "didn't raise RuntimeError (select mutating the list)"
    except RuntimeError:
        pass
