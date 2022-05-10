import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(f.fileno())
    select.select([f], [], [])

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            test_select_closed()
            return a.pop()

    f = F()
    a.append(f.fileno())
    select.select([f], [], [])

def test_select_closed_pipe():
    a = []

    class F:
        def fileno(self):
            test_select_closed_pipe()
            return a.pop()

    f = F()
    a.append(f.fileno())
    select.select([f], [], [])

def test_select_closed_pipe_2():
    a = []

    class F:
        def fileno(self):
            test_select_closed_pipe_2()
            return a.pop()

    f = F()
    a.append(f.fileno())
