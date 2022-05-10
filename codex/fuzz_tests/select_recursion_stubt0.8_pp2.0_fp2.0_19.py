import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    class B:
        fileno = a.append

    a = range(10)
    s = set([F(), B()])
    assert select.select(s, [], [], 0) == ([], [], [])
