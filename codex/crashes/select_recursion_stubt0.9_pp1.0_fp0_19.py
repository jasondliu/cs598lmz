import select
def test_select_mutated():
    class F:
        def fileno(self):
            test_select_mutated()
    s = select.select([F()], [], [], 0.1)
test_select_mutated()
