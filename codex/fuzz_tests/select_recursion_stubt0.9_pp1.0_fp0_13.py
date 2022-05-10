import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a) 
    sel = select.select

    with pytest.raises(RuntimeError):
        sel([F()], [], [])

@pytest.mark.skipif(sys.platform == "win32", reason="POSIX-specific behavior")
def test_file_in():
    f = open(__file__, 'rb')
    assert select.select([f], [f], [f], 0) == ([f], [f], [f])
    f.close()

    # f has been closed, but the C code still thinks it should be used for
    # waiting.
    with pytest.raises(select.error) as cm:
        select.select([f], [f], [f], 0)
    exc = cm.value
    assert exc.args == ((errno.EBADF, "Bad file descriptor"),)


def _test_simple_buf_len(n):
    # A few simple tests to check that the buf_len is correct
    buf = bytearray(b'x') * n
    f = open
