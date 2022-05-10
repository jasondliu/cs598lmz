import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(self)
            return 1

    assert select.select([F()], [], [], 1.0) == ([], [], [])
    assert a == []
    raises(ValueError, select.select, [], [F()], [], 1.0)
    assert a == []
    raises(ValueError, select.select, [], [], [F()], 1.0)
    assert a == []


def test_select_large_fd():
    try:
        import resource
    except ImportError:
        skip("no resource module")

    old = resource.getrlimit(resource.RLIMIT_NOFILE)
    try:
        resource.setrlimit(resource.RLIMIT_NOFILE, (1, old[1]))
        raises(ValueError, select.select, [0], [], [], 0.1)
    finally:
        resource.setrlimit(resource.RLIMIT_NOFILE, old)


class TestSelect:

    def test_rlist_not_modified(self):
        fd = os.open
