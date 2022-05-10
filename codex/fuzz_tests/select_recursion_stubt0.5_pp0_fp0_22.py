import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    try:
        select.select(a, a, a)
    except RuntimeError:
        pass

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            return 0

    a.append(F())
    try:
        select.select(a, a, a)
    except RuntimeError:
        pass

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            return 0

    a.append(F())
    try:
        select.select(a, a, a)
        select.select(a, a, a)
    except RuntimeError:
        pass

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            return 0

    a.append(F())
    try:
        select.select(a, a, a)
        select.select(a, a, a)
        select.select
