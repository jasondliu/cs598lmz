import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            raise AssertionError("should not be used")

    select.select([F()], [F()], [F()])
    test_select_mutated()
    select.select([F()], [F()], [F()])

def test_select_keyboardinterrupt_read():
    class F:
        def fileno(self):
            raise KeyboardInterrupt
    try:
        select.select([F()], [], [])
        raise AssertionError("should have raised")
    except KeyboardInterrupt:
        pass

def test_select_keyboardinterrupt_write():
    class F:
        def fileno(self):
            raise KeyboardInterrupt
    try:
        select.select([], [F()], [])
        raise AssertionError("should have raised")
    except KeyboardInterrupt:
        pass

def test_select_keyboardinterrupt_except():
    class F:
        def fileno(self):
            raise KeyboardInterrupt
    try:
        select.select([], [], [F()])
        raise Assert
