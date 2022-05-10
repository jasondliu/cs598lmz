import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def close(self):
            a.append(1)

    f = F()
    try:
        select.select([f], [], [], 0)
    except ValueError:
        pass
    assert a == [1]

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 0

        def close(self):
            a.append(1)

    f = F()
    f.close()
    try:
        select.select([f], [], [], 0)
    except ValueError:
        pass
    assert a == [1]

def test_select_closed_after():
    a = []

    class F:
        def fileno(self):
            return 0

        def close(self):
            a.append(1)

    f = F()
    try:
        select.select([f], [], [], 0)
    except ValueError:
        pass
    assert a == [1]

