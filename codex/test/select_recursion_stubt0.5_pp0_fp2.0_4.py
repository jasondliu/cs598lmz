import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
        assert False, "should have raised RuntimeError"
    except RuntimeError:
        pass

def test_select_large():
    a, b, c = [], [], []
    for i in range(1024):
        a.append(i)
        b.append(i + 1024)
        c.append(i + 2048)
    select.select(a, b, c)
