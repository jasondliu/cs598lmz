import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    def f():
        select.select([F()], [], [])

    a = [0]
    raises(ValueError, f)
    a = [1]
    raises(ValueError, f)
    a = [2]
    raises(ValueError, f)
    a = [3]
    raises(ValueError, f)
    a = [4]
    raises(ValueError, f)
    a = [5]
    raises(ValueError, f)
    a = [6]
    raises(ValueError, f)
    a = [7]
    raises(ValueError, f)
    a = [8]
    raises(ValueError, f)
    a = [9]
    raises(ValueError, f)
    a = [10]
    raises(ValueError, f)
    a = [11]
    raises(ValueError, f)
    a = [12]
    raises(ValueError, f)
    a = [13]
    raises(ValueError, f)
