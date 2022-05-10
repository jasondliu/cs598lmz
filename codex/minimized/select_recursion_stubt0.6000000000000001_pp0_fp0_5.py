import select
def test_select_mutated():
    a = []
    class F:
        def fileno(self):
            test_select_mutated()
    a.append(F())
    select.select([], a, [], 0)
test_select_mutated()
