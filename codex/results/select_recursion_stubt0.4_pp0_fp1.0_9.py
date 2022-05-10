import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    class G:
        def fileno(self):
            return a.pop()

    f = F()
    g = G()
    a = [f, g]
    select.select([f], [], [], 0)
