import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def read(self):
            a.append(1)

    def check():
        try:
            select.select([F()], [], [], 0)
        except NameError:
            pass

    check()
    res = []
    for i in range(50):
        res.append(a)
        a = []
    for a, b in zip(res, res[1:]):
        assert a == b
