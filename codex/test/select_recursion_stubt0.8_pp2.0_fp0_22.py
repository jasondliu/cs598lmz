import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    r, w, x = select.select([F()], [F()], [F()])
    assert len(r) == 0
    assert len(w) == 0
    assert len(x) == 0

def test_select_interrupt():
    a = []
    b = []
    c = []
    d = []

    class F1:
        def fileno(self):
            test_select_interrupt()
            return a.pop()
    class F2:
        def fileno(self):
            test_select_interrupt()
            return b.pop()
    class F3:
        def fileno(self):
            test_select_interrupt()
            return c.pop()
    class F4:
        def fileno(self):
            test_select_interrupt()
            return d.pop()
    try:
        select.select([F1()], [F2()], [F3()])
    except ValueError:
        pass
