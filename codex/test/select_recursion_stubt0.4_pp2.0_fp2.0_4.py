import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    try:
        select.select([F()], [], [])
    except ValueError:
        pass
    else:
        print("ValueError not raised")

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            test_select_closed()
            return a.pop()

    try:
        select.select([F()], [], [])
    except ValueError:
        pass
    else:
        print("ValueError not raised")

def test_select_closed_after_fileno():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    try:
        select.select([F()], [], [])
    except ValueError:
        pass
    else:
        print("ValueError not raised")

def test_select_closed_after_fileno_in_list():
    a = []

    class F:
        def fileno(self):
            return a.pop()

