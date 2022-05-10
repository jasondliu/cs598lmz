import select
def test_select_mutated():
    class F:
        def fileno(self):
            test_select_mutated()
    select.select([], [], [F()])
test_select_mutated()
