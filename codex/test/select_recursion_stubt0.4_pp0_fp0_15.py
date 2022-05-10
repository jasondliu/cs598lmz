import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(f.fileno())
    try:
        select.select([f], [], [])
    except IndexError:
        pass

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    a.append(f.fileno())
    try:
        select.select([f], [], [])
    except ValueError:
        pass

def test_poll_mutated():
    a = []

    class F:
        def fileno(self):
            test_poll_mutated()
            return a.pop()

    f = F()
    a.append(f.fileno())
    try:
        select.poll()
    except IndexError:
        pass

def test_poll_closed_fd():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
