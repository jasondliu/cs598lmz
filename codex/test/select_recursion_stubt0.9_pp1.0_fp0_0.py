import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    for i in xrange(1000):
        a.append(F())
        b = select.select([], [], a, 0.01)
