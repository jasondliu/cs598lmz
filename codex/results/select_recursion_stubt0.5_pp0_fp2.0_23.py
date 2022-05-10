import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    f = F()
    select.select([f], [f], [f], 0.0)

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1
    f = F()
    select.select([f], [f], [f], 0.0)

def test_select_mutated3():
    class F:
        def fileno(self):
            return 1
    f = F()
    select.select([f], [f], [f], 0.0)
    f.fileno = lambda: 1/0
    select.select([f], [f], [f], 0.0)

def test_select_mutated4():
    class F:
        def fileno(self):
            return 1
    f = F()
    select.select([f], [f], [f], 0.0)
    f.fileno = lambda: 1/0
    try:
        select.select([f], [f],
