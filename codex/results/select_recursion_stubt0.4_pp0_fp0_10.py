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
    f()
    a = [1, 0]
    f()
    a = [1, 0, 2]
    f()
    a = [1, 0, 2, 3]
    f()
    a = [1, 0, 2, 3, 4]
    f()
    a = [1, 0, 2, 3, 4, 5]
    f()
    a = [1, 0, 2, 3, 4, 5, 6]
    f()
    a = [1, 0, 2, 3, 4, 5, 6, 7]
    f()
    a = [1, 0, 2, 3, 4, 5, 6, 7, 8]
    f()
    a = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]
    f()
    a = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    f
