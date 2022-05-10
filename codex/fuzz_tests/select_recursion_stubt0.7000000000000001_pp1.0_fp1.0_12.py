import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1
        def close(self):
            a.append(1)

    class G:
        def __enter__(self):
            a.append(1)
        def __exit__(self, *args):
            a.append(1)

    with G():
        select.select([F()], [F()], [F()], 0)
    assert a == [1, 1, 1, 1, 1, 1]

def test_pipe():
    r, w = os.pipe()
    assert r != w
    assert r >= 0
    assert w >= 0
    for fd in (r, w):
        assert os.write(fd, b"a") == 1
        assert os.read(fd, 1) == b"a"
        os.close(fd)
    with pytest.raises(OSError):
        os.read(r, 1)
    with pytest.raises(OSError):
        os.write(w, b"a")

def test_fd_leak():
    # https://bugs.python.org
