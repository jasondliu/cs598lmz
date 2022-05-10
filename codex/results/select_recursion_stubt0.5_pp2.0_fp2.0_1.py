import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    select.select([], [F()], [])

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return len(a)
    select.select([], [F()], [])

class F:
    def fileno(self):
        return 0

class G:
    def fileno(self):
        return 1

def test_select_mutated_3():
    select.select([F()], [G()], [])

def test_select_mutated_4():
    select.select([F()], [G()], [], 0.0)

def _test_select_mutated_5():
    select.select([F()], [G()], [], 0.0, 0.0)

def test_select_mutated_6():
    select.select([F()], [G()], [], 0.0, None)

def test_select_mutated_7():
    select.
