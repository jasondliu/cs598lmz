import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return sys.stdin.fileno()

    fd = select.select([F()], [], [], 0.0)
    del fd
    gc.collect()

test_select_mutated()
