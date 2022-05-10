import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([a], [a], [a], 0)
    select.select([F()], [a], [a], 0)
    select.select([a], [F()], [a], 0)
    select.select([a], [a], [F()], 0)
    select.select([a], [a], [a], 0)
    select.select([F()], [a], [a], 0)
    select.select([a], [F()], [a], 0)
    select.select([a], [a], [F()], 0)

test_select_mutated()
