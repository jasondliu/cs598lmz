import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [], 0)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            a.append(self)
            return self

        def close(self):
            a.remove(self)

    select.select([F()], [], [], 0)

def test_select_returns_closed():
    a = []

    class F:
        def fileno(self):
            a.append(self)
            return self

        def close(self):
            a.remove(self)

    select.select([F()], [], [], 0)

def test_select_returns_invalid():
    a = []

    class F:
        def fileno(self):
            a.append(self)
            return self

        def close(self):
            a.remove(self)

    select.select([F()], [], [], 0)

def test_select_returns_bad_fd():
    a = []
