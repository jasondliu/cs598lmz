import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a = [f]
    select.select([f], [], [], 1.0)

def test_select_error():
    a = []

    class F:
        def fileno(self):
            test_select_error()
            return a.pop()

    f = F()
    a = [f]
    try:
        select.select([f], [], [], 1.0)
    except ValueError:
        pass
    else:
        raise AssertionError("Didn't raise ValueError")

def test_kevent_mutated():
    a = []

    class F:
        def fileno(self):
            test_kevent_mutated()
            return a.pop()

    f = F()
    a = [f]
    select.kqueue()
    select.kevent([f], [], [], 1.0)

def test_kevent_error():
    a = []

    class F:
        def fileno(self):
            test_ke
