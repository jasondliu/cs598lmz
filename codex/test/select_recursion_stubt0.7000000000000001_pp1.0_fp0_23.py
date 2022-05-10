import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()

    for i in range(10):
        a.append(i)
        select.select([f], [], [])

def test_select_listener_mutated():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()

    for i in range(10):
        a.append(i)
        select.select([f], [], [])

def test_select_writer_mutated():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()

    for i in range(10):
        a.append(i)
        select.select([], [f], [])

def test_select_exceptional_mutated():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()

    for i in range(10):
        a.append(i)
