import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def replace():
        del a[:]
        a.extend([F(), F()])
    replace()
    select.select([a[0]], [], [], 0)
    replace()
    select.select([a[0]], [], [], 0)
