import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([], F(), [])
    return a

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            return 0

    select.select([], F(), [])
    return a

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            return 0

    select.select([], F(), [])
    return a

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            return 0

    select.select([], F(), [])
    return a

def test_select_mutated5():
    a = []

    class F:
        def fileno(self):
            return 0

    select.select([], F(), [])
    return a
