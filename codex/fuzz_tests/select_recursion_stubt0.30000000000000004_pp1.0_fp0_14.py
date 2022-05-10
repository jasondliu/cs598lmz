import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return f.fileno()
    f = F()
    a.append(f)
    select.select(a, a, a)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            return f.fileno()
    f = F()
    a.append(f)
    select.select(a, a, a)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            return f.fileno()
    f = F()
    a.append(f)
    select.select(a, a, a)

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            return f.fileno()
    f = F()
    a.append(f)
    select.select(a, a, a)

def test_select_mutated_5():
    a = []

    class F:
        def fileno(self
