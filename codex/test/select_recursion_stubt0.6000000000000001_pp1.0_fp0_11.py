import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    def f():
        select.select([F()], [], [])

    a.append(1)
    raises(ValueError, f)
    a.append(2)
    raises(ValueError, f)
    a.append(3)
    raises(ValueError, f)
    a.append(4)
    raises(ValueError, f)

    class F:
        def fileno(self):
            return a.pop()

    def f():
        select.select([F()], [], [])

    a.append(1)
    raises(ValueError, f)
    a.append(2)
    raises(ValueError, f)
    a.append(3)
    raises(ValueError, f)
    a.append(4)
    raises(ValueError, f)

def test_select_invalid_fd():
    raises(ValueError, select.select, [5], [], [])
    raises(ValueError, select.select, [], [5], [])
