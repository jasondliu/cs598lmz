import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([a], [a], [a], 0)
    select.select([a], [a], [a], 0)
    select.select([a], [a], [a], 0)
    select.select([F()], [a], [a], 0)
    select.select([a], [a], [a], 0)
    select.select([a], [a], [a], 0)
    select.select([a], [a], [a], 0)

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return 0

    select.select([a], [a], [a], 0)
    select.select([a], [a], [a], 0)
    select.select([a], [a], [a], 0)
    select.select([a], [a], [a], 0)
    select.select([a], [a], [a], 0)
    select.select([a], [a], [a], 0
