import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    with pytest.raises(IndexError):
        select.select([F()], [], [])

    with pytest.raises(IndexError):
        select.select([], [F()], [])

    with pytest.raises(IndexError):
        select.select([], [], [F()])

def test_select_error():
    class F:
        def fileno(self):
            return 42

        def read(self):
            raise ValueError

    rlist = [F()]
    with pytest.raises(select.error) as excinfo:
        select.select(rlist, [], [])
    assert excinfo.value.args == (42, 'File descriptor was closed in another greenlet')
    assert rlist == []

def test_select_error_timeout():
    class F:
        def fileno(self):
            return 42

        def read(self):
            raise ValueError

    rlist = [F()]
