import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            del a[:]

    select.select([F()], [F()], [F()], 0.0)

class F:
    def fileno(self):
        return 5

class G:
    def fileno(self):
        raise OSError

def test_select_error():
    select.select([G()], [G()], [G()], 0.0)

class H:
    def fileno(self):
        raise ValueError

def test_select_error2():
    select.select([H()], [H()], [H()], 0.0)

def test_select_badargs():
    select.select(1, [2], 3, 4)

def test_select_badargs2():
    select.select([1], 2, 3, 4)

def test_select_badargs3():
    select.select([1], [2], 3, 4)

def test_select_badargs4():
    select.select(1, [2], [3], 4)

def test_poll_badargs
