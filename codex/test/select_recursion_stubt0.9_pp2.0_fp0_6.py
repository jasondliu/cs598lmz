import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

            a.append(self)
            return 1

    r = select.select([], [F()], [])
    assert r[1] is not None
    assert a == r[1]
    # Should not crash


def test_timeout():
    select.select([], [], [], 0.0) # Should not raise an exception


def test_descriptor_higher_64k():
    """Issue 1813: select shouldn't throw OverflowError on
    higher valued descriptors."""
    fd = os.open(os.devnull, os.O_RDONLY)
    try:
        ur = unix_select.unix_select([fd], [], [], 0.0)
        assert ur == ([fd], [], []), ur
    finally:
        os.close(fd)
