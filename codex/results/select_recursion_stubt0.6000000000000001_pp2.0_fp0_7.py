import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    def g(x):
        a.append(x)
        return x

    select.select([F()], [], [], 1)
    select.select([F()], [], [], 1)
    select.select([F()], [], [], 1)
    select.select([F()], [], [], 1)
    select.select([F()], [], [], 1)
    select.select([F()], [], [], 1)
    select.select([F()], [], [], 1)
    select.select([F()], [], [], 1)
    select.select([F()], [], [], 1)
    select.select([F()], [], [], 1)
    select.select([F()], [], [], 1)
    select.select([F()], [], [], 1)
    select.select([F()], [], [], 1)
    select.select([F()], [], [], 1)
    select.select([F()], [], [], 1)
    select.select([F
