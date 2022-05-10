import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
        def read(self, n):
            a.append(n)
            return b""

    select.select([F()], [], [], 0)
    select.select([F()], [], [], 0)
    # we should not get an error from trying to access the socket a second time
    assert len(a) == 2
