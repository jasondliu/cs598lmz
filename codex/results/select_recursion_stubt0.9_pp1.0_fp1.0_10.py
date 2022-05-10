import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 100

    class G:
        def fileno(self):
            a.append(None)
            return 101

    select.select([F()], a, a, 0)
    select.select([F()], a, a, 1)
    select.select([G()], a, a, 0)
    select.select([G()], a, a, 1)
