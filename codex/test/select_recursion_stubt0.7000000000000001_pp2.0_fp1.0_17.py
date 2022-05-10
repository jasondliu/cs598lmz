import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def close(self):
            a.append(1)

    f = F()
    select.select([], [], [])
    f.close()

test_select_mutated()

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return len(a)
        def close(self):
            a.append(1)

    f = F()
    select.select([], [], [f])
    f.close()

test_select_mutated_2()

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return len(a)
        def close(self):
            a.append(1)

    f = F()
    select.select([f], [], [])
    f.close()

test_select_mutated_3()

