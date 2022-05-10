import select
def test_select_mutated():
    class F:
        def fileno(self):
            test_select_mutated()
    r = select.select([F()], [], [])
test_select_mutated()
