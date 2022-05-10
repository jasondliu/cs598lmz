import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return int(a[0])

    fd = select.select([F()], [], [], 0.1)
    assert not fd[0]


def test_select_interrupted():
    skip("XXX issue #6059 need to review this test")
    a = []

    def fileno():
        if a:
            return int(a[0])
        raise ValueError

    fd = select.select([fileno], [], [], 0.1)
    assert not fd[0]
