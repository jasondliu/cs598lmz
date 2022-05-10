import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a = [f]
    select.select([f], [], [])

def test_select_del():
    a = []

    class F:
        def fileno(self):
            del a[:]
            return a.pop()

    f = F()
    a = [f]
    select.select([f], [], [])

def test_select_close():
    a = []

    class F:
        def fileno(self):
            a.pop().close()
            return a.pop()

    f = F()
    a = [f]
    select.select([f], [], [])

def test_select_iter():
    a = []

    class F:
        def fileno(self):
            a.append(a[0])
            return a.pop()

    f = F()
    a = [f]
    select.select([f], [], [])

def test_select_len():
    a = []

    class F:
        def
