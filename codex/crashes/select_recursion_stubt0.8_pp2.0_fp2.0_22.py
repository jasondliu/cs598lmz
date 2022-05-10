import select
def test_select_mutated():
    class F:
        def fileno(self):
            test_select_mutated()
    fd = select.select([F()], [], [], 0.0)
test_select_mutated()
