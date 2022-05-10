import select
def test_select_mutated():
    a = []
    class F:
        def fileno(self):
            test_select_mutated()
    a.append(F())
    try:
        select.select([], [], a, 0)
    except:
        pass
test_select_mutated()
