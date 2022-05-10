import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    assert select.select([], [], [F()], 1)

def test_select_error():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            raise OSError(errno.EBADF, "uhoh")
    r, w, x = select.select([F()], [], [], 1)
    assert r == w == x == []
    assert a == [1]

def test_select_bad_type():
    raises(TypeError, "select.select(1, 2, 3, 4)")
    raises(TypeError, "select.select(1, 2, [])")
    raises(TypeError, "select.select([], 2, 3)")
    raises(TypeError, "select.select([], 2, [])")
    raises(TypeError, "select.select([], [], 2)")
    raises(TypeError, "select.select([], [], [], 'x')")

#def test_select_bad_fd():

