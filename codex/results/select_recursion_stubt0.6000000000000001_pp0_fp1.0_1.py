import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1

    select.select([F()], [], [], 0)
    assert a == [1]

def test_select_non_integer_fd():
    class F:
        def fileno(self):
            return "1"

    raises(TypeError, select.select, [F()], [], [], 0)

def test_select_negative_fd():
    class F:
        def fileno(self):
            return -1

    raises(ValueError, select.select, [F()], [], [], 0)

def test_select_invalid_fd():
    class F:
        def fileno(self):
            return 1

    raises(OSError, select.select, [F()], [], [], 0)
