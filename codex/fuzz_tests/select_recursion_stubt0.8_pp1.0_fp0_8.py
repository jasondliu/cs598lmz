import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(f)
            return f.fileno()
    f = F()
    p = select.poll()
    p.register(f)
    p.poll()

def test_poll_mutated():
    a = []

    class F:
        def fileno(self):
            test_poll_mutated()
            a.append(f)
            return f.fileno()
    f = F()
    p = select.poll()
    p.register(f)
    p.poll()
