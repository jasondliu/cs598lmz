import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f():
        a.append(1)
        return 1

    select.select([], [], [], 0.0)
    select.select([f], [], [], 0.0)
    assert a == [1]
    a = []
    select.select([F()], [], [], 0.0)
    assert a == []


def test_select_closed_fd():
    # Issue #15133
    fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    fd.close()
    try:
        select.select([fd], [], [], 0.0)
    except OSError:
        pass
    else:
        assert False, "select.select() worked on a closed fd"
