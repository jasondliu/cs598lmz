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
        select.select([], [], [], 0)
    except ValueError:
        pass
    a.remove(f)
    try:
        select.select([], [], [], 0)
    except ValueError:
        pass

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 0
        def close(self):
            a.remove(self)

    f = F()
    a.append(f)
    try:
        select.select([], [], [], 0)
    except ValueError:
        pass
    f.close()
    try:
        select.select([], [], [], 0)
    except ValueError:
        pass

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            return 0
        def close(self):
            a.remove(self)

    f = F()
    a.
