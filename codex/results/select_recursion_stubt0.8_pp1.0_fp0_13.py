import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            del a[0]
            return 1
        def recv(self, *args):
            del a[0]
            test_select_mutated()
            return b""

    a[:] = [F()]
    a.append(a[0])
    select.select([a[0]], [], [], 0)
    return a

def test_delay_mutated():
    a = []

    class F:
        def fileno(self):
            a[0] = 1
            return test_delay_mutated()
        def recv(self, *args):
            a[0] = 1
            return test_delay_mutated()

    a[:] = [F()]
    a.append(a[0])
    select.select([a[0]], [], [], 0)
    return a
