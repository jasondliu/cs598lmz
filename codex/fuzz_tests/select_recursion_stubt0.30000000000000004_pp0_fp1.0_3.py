import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass

    a.append(F())
    select.select([], [], [])

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return len(a)
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass

    a.append(F())
    select.select([], [], [], 1)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return len(a)
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass

    a.append(F())
    select.select([], [], [], 1, 1)

def test_
