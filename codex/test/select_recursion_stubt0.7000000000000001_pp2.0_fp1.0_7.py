import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 5

    a.append(F())

    for fd in select.select([], a, [], 1)[1]:
        pass

def test_select_exception():
    a = []

    class F:
        def fileno(self):
            raise ValueError("fileno")

    a.append(F())

    try:
        r, w, x = select.select([], a, [], 1)
    except ValueError:
        pass
    else:
        assert False, "should've raised"

def test_select_except_EBADF():
    a = []

    class F:
        def fileno(self):
            return 5

    a.append(F())

    def bad_fileno():
        for fd in select.select([], a, [], 1)[1]:
            pass

    def bad_close():
        os.close(5)

    assert_raises(OSError, bad_fileno)
    assert_raises(OSError, bad_close)


# test_select_except_EBADF()
