import select
def test_select_mutated():
    a = []
    class F:
        def fileno(self):
            test_select_mutated()
    f = F()
    a.append(f)
    for i in range(4):
        try:
            select.select(a, [], [])
        except RuntimeError as e:
            print(e)
test_select_mutated()
