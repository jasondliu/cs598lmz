import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def read(self, size):
            a.append(1)
            return b'x'

    r, w, x = select.select([F()], [], [], 0.1)
    assert a == [1]
