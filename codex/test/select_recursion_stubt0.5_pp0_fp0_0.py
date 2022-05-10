import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 5
    select.select([F()], [], [], 1)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 5
    select.select([F()], [], [], 1)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 5
        def close(self):
            a.append(2)
            return 5
    select.select([F()], [], [], 1)

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 5
        def close(self):
            a.append(2)
            return 5
        def __del__(self):
            a.append(3)
            return 5
    select.select([F()], [], [], 1)

