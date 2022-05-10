import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    def g():
        a.append(1)

    s = select.select([F()], [], [])

    # test that fd_sets are not mutated (see issue #11649)
    assert s == ([], [], [])
    # test that the callbacks are not triggered
    assert a == []

def test_select_mutated_error():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            raise ValueError

    def g():
        a.append(1)

    s = select.select([F()], [], [])

    # test that fd_sets are not mutated (see issue #11649)
    assert s == ([], [], [])
    # test that the callbacks are not triggered
    assert a == []
