import select
def test_select_mutated():
    a = []
    class F:
        def fileno(self):
            test_select_mutated()
    a.append(F())
    select.select([], a, [])
test_select_mutated()
