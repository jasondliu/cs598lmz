import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    f = F()
    a.append(f)
    try:
        select.select([f], [], [], 0)
    except ValueError:
        pass
    else:
        raise Exception("select() didn't raise ValueError")

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 1

    f = F()
    a.append(f)
    try:
        select.select([f], [], [], 0)
    except ValueError:
        pass
    else:
        raise Exception("select() didn't raise ValueError")

def test_select_closed_and_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_closed_and_mutated()
            return 1

    f = F()
    a.append(f)
    try:
        select.select([f], [], [], 0)
    except ValueError:
        pass
    else:
        raise Exception("select() didn't raise
