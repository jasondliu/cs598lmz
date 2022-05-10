import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    f = F()
    a.append(f.fileno())
    select.select([f], [], [], 1)

def test_select_mutated_timeout():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_timeout()
            return a.pop()
    f = F()
    a.append(f.fileno())
    select.select([f], [], [], 1)

def test_select_mutated_timeout_error():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_timeout_error()
            return a.pop()
    f = F()
    a.append(f.fileno())
    select.select([f], [], [], 1)

def test_select_mutated_error():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_error()
            return a.pop()
    f = F()

