import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    a.append(F())
    select.select(a, [], [], 0)

# one select tests passed!

def test_select_unregistered():
    a = []

    class F:
        def fileno(self):
            return -1

    a.append(F())
    select.select(a, [], [], 0)

# two select tests passed!

def test_select_bad_keyword():
    a = []
    select.select(a, [], [], 0, foo=1)

# three select tests passed!
