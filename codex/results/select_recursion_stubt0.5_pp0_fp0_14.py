import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    class S:
        def __getitem__(self, n):
            return F()

    s = S()
    a.append(1)
    select.select(s, s, s, 0)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return len(a)

    class S:
        def __getitem__(self, n):
            return F()

    s = S()
    a.append(1)
    select.select(s, s, s, 0)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return len(a)

    class S:
        def __getitem__(self, n):
            return F()

    s = S()
    a.append(1)
    select.select(s, s, s, 0)


