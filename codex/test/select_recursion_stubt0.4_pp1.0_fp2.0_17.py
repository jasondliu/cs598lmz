import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    try:
        select.select([f], [], [], 1)
        a.append(1)
    except RuntimeError:
        a.append(2)
    assert a == [2]

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 0

    f = F()
    try:
        select.select([f], [], [], 1)
        a.append(1)
    except RuntimeError:
        a.append(2)
    assert a == [2]

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return 0

    f = F()
    try:
        select.select([f], [], [], 1)
        a.append(1)
    except RuntimeError:
        a.append(2)
