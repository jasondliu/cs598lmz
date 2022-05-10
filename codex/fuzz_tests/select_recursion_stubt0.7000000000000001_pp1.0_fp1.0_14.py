import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [])
    raises(ValueError, select.select, [F()], [], [])

def test_select_closed_fd():
    class F:
        def fileno(self):
            return 3

    select.select([F()], [], [])

def test_select_three_args():
    raises(TypeError, select.select, [], [], [], [])

def test_select_bad_timeout():
    raises(TypeError, select.select, [], [], [], "foo")

def test_select_error_fileno():
    class F:
        def fileno(self):
            raise OSError
    raises(OSError, select.select, [F()], [], [])

def test_select_error_poll():
    class F:
        def fileno(self):
            return 3
    select.select([F()], [], [])
    class F:
        def fileno(self):
            return 4
    select.select
