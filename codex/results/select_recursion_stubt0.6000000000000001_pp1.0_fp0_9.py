import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    f = F()
    a = [f.fileno()]
    select.select([f], [], [], 0)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            test_select_closed()
            return a.pop()
    f = F()
    a = [f.fileno()]
    select.select([f], [], [], 0)

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_closed_mutated()
            return a.pop()
    f = F()
    a = [f.fileno()]
    select.select([f], [], [], 0)

def test_select_closed_mutated_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_closed_mutated_mutated()
            return a.pop()
    f = F()
    a = [
