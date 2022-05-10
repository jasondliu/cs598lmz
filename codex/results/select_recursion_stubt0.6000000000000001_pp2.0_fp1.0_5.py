import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    class G:
        def fileno(self):
            return 0

    a.append(F())
    a.append(G())
    select.select(a, [], [])
    print("OK")
