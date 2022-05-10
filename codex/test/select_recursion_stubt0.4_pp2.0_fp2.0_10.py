import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    select.select([F()], [], [], 0)
    a.append(1)
    select.select([], [F()], [], 0)
    a.append(2)
    select.select([], [], [F()], 0)
    a.append(3)
    assert a == [1, 2, 3]

def test_select_closed_fd():
    import os
    import socket
    import select

    fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    fd.close()
    try:
        select.select([fd], [], [], 0)
    except ValueError:
        pass
    else:
        assert False, "select.select() with closed fd didn't raise ValueError"

def test_select_closed_pipe():
    import os
    import select

    r, w = os.pipe()
    os.close(w)
    try:
        select.select([r], [], [], 0)
    except ValueError:
        pass
