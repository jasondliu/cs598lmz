import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    try:
        select.select([F()], a, a, 0)
    except ValueError:
        pass
    else:
        assert False, "should have raised ValueError"
    try:
        select.select(a, [F()], a, 0)
    except ValueError:
        pass
    else:
        assert False, "should have raised ValueError"
    try:
        select.select(a, a, [F()], 0)
    except ValueError:
        pass
    else:
        assert False, "should have raised ValueError"

def test_select_closed_pipe():
    r, w = os.pipe()
    try:
        os.close(w)
        assert select.select([r], [], [], 0) == ([r], [], []), "select on closed pipe should not raise exception"
    finally:
        os.close(r)

def test_select_closed_file():
    f = open(test_support.TESTFN, 'w')
    try:
        f.close()

