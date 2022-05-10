import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    class G:
        def fileno(self):
            a.append(1)
            return 2

    sel = selectors.DefaultSelector()
    sel.register(F(), select.EPOLLIN)
    sel.register(G(), select.EPOLLIN)
    for key, event in sel.select(0):
        pass
    assert len(a) == 1

def test_select_not_mutated():
    a = []

    class F:
        def fileno(self):
            return 1

    class G:
        def fileno(self):
            a.append(1)
            return 2

    sel = selectors.DefaultSelector()
    sel.register(F(), select.EPOLLIN)
    sel.register(G(), select.EPOLLIN)
    for key, event in sel.select(0):
        pass
    assert len(a) == 1
