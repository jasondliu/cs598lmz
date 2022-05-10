import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

        def read(self):
            a.append(1)

    with pytest.raises(RuntimeError):
        select.select([], [F()], [])
    assert not a

# Issue9791: make sure select() doesn't modify its arguments
def test_select_nonmutating():
    r = [None]
    w = [None]
    x = [None]
    ret = select.select(r, w, x)
    assert ret == ([], [], []), ret

def test_select_error():
    # If any file descriptor is negative, select.error is raised
    with pytest.raises(select.error):
        select.select([-1], [], [])
    with pytest.raises(select.error):
        select.select([], [-1], [])
    with pytest.raises(select.error):
        select.select([], [], [-1])

def test_select_bad_fd():
    with pytest.raises(ValueError):
        select.select([object()
