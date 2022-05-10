import select
def test_select_mutated():
    a = []
    class F:
        def fileno(self):
            test_select_mutated()
    for i in range(1000):
        a.append(F())
    select.select(a, [], [])
test_select_mutated()
