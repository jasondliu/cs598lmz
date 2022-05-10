import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
        def close(self):
            a.append(1)
            test_select_mutated()
            a.append(3)

    s = select.poll()
    def g():
        s.register(F())

    g()
    assert a == [1, 3]
