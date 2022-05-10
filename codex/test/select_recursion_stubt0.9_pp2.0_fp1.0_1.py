import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 42

    with raises(BlockingIOError):
        select.select([F()], [], [], 0)

    assert a == []
