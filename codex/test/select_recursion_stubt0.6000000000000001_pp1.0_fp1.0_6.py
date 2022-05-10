import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)
    try:
        select.select(a, a, a, 0)
    finally:
        a.clear()

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return 0

    f = F()
    a.append(f)
    try:
        select.select(a, a, a, 0)
    finally:
        a.pop()

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return 0

    f = F()
    a.append(f)
    try:
        select.select(a, a, a, 0)
    finally:
        a[0] = None

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated
