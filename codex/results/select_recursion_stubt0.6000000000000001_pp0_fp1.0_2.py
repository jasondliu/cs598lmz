import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    f = F()
    fd = f.fileno()
    a.append(1)
    assert select.select([f], [f], [f], 0.0) == ([f], [f], [f])
    assert f.fileno() == fd
