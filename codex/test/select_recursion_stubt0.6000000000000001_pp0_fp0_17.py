import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    class E:
        def fileno(self):
            a.append(1)
            return 2

    r, w, x = select.select([F()], [], [E()], 0)
    assert r == w == x == []
    assert a == [1]

def test_select_bad_fd():
    class F:
        def fileno(self):
            return "1"

    try:
        select.select([F()], [], [], 1)
    except ValueError:
        pass
    else:
        py.test.fail("ValueError not raised")

def test_select_closed_pipe():
    r, w = os.pipe()
    try:
        os.close(w)
        select.select([r], [], [], 0)
    finally:
        os.close(r)

def test_select_closed_pipe_in_list():
    r, w = os.pipe()
