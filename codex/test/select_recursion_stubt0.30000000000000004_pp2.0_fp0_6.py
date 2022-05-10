import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def read(self):
            a.append(1)
            return 1
        def write(self):
            a.append(1)
            return 1
        def close(self):
            a.append(1)

    select.select([F()], [F()], [F()], 0)
    assert a == [1, 1, 1]

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return len(a)
        def read(self):
            a.append(1)
            return 1
        def write(self):
            a.append(1)
            return 1
        def close(self):
            a.append(1)

    select.select([F()], [F()], [F()], 0)
    assert a == [1, 1, 1]

def test_select_mutated_3():
    a = []

