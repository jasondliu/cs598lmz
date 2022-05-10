import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    def g():
        a.append(F())
        return a[-1]

    select.select([g()], [], [], 0)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return len(a)

        def close(self):
            a.append(None)

    def g():
        a.append(F())
        return a[-1]

    select.select([g()], [], [], 0)

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            return len(a)

        def close(self):
            a.append(None)

    def g():
        a.append(F())
        return a[-1]

    select.select([g()], [], [], 0)
    a[0].close()

def test_select_closed_mutated_2():
    a = []

