import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    select.select([F()], [], [], 0)
    assert not a, "select mutated arguments"
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    select.select([F()], [], [], 0)
    assert not a, "select mutated arguments"


def test_select_on_invalid_fd():
    class F:
        def fileno(self):
            return -1
    try:
        select.select([F()], [], [], 0)
    except ValueError:
        pass
    else:
        assert False, "select() accept a fd < 0"
test_select_on_invalid_fd.need_sock = True


def test_select_on_closed_fd():
    r, w = os.pipe()
    os.close(r)
    os.close(w)
    try:
        select.select([r], [], [], 0)
    except ValueError:
