import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 4

    a.append(F())
    try:
        select.select([],[],a)
    except ValueError:
        # the file descriptor was closed
        pass
    else:
        assert 0, 'expected ValueError'
