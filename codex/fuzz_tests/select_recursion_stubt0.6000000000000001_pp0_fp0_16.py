import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    f = F()
    a.append(f)

    try:
        select.select([f], [], [])
    except ValueError:
        pass

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return len(a)

    f = F()
    a.append(f)

    try:
        select.select([f], [], [])
    except ValueError:
        pass

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            return len(a)

        def close(self):
            a.clear()

    f = F()
    a.append(f)

    try:
        select.select([f], [], [])
    except ValueError:
        pass

def test_select_negative():
    a = [-1]

    class F:
        def fileno(self):
            return len(a)

    f = F()
    a.append(
