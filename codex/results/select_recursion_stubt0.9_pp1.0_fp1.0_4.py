import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # bpo-39096: must not be cached
            return a.pop()

    f = [F(), F(), F(), F()]
    select.select([f[2]], [f[1]], [f[3]])
    select.select([f[0]], [f[0]], [f[4]])
