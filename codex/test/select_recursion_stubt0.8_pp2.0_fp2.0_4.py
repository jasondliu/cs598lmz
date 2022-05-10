import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 100

    class G:
        def fileno(self):
            return 100500

    sel = select.select([F(), G()], [], [])
