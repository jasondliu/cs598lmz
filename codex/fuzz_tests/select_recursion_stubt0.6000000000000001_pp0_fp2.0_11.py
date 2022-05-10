import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return None

    select.select([], [F()], [])
    a.append(1)
    assert a == [1]

def test_select_keyboardinterrupt():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            raise KeyboardInterrupt
            return None

    try:
        select.select([], [F()], [])
    except KeyboardInterrupt:
        pass
    assert a == [1]

def test_select_oserror():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            raise OSError
            return None

    try:
        select.select([], [F()], [])
    except OSError:
        pass
    assert a == [1]

def test_select_non_int():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return "hello"

    try:
        select.select([], [F
