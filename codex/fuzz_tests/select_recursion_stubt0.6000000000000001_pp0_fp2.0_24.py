import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    select.select([], a, a)

def test_select_mutated2():
    a = []
    a.append([])
    select.select([], a, a)

def test_select_mutated3():
    a = []
    class F:
        def fileno(self):
            a.pop()
            return 0
    a.append(F())
    select.select([], a, a)

def test_select_mutated4():
    import os
    a = []
    a.append(os.open('/dev/null', os.O_RDONLY))
    select.select([], a, a)

def test_select_mutated5():
    import os
    a = []
    a.append(os.open('/dev/null', os.O_RDONLY))
    select.select([], a, a, timeout=0.1)

def test_select_mutated6():
    import os
    a = []
    a.append(
