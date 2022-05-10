import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

        def close(self):
            del a[0]

    a.append(F())
    try:
        select.select([F()], [], [])
    except RuntimeError, e:
        assert str(e) == "I/O operation on closed file", str(e)
    assert len(a) == 0, str(len(a))

def test_issue_5554():
    fd = os.open(".", os.O_RDONLY)
    try:
        # This should not raise an OSError.
        select.select([fd], [fd], [fd], 0)
    finally:
        os.close(fd)
