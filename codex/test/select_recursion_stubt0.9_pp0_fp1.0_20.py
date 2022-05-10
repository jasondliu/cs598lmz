import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    r = [F(), F()]
    g = select.select([], r, [], 0)
    for f in r:
        f.close()
