import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            self.a.append(1)
            return a.pop()

    def g():
        return test_select_mutated()
    F.a = a
    f = F()
    try:
        select.select([f], [f], [f], 0.0)
    except IndexError:
        pass
