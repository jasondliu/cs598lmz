import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    f = F()
    r, w, x = select.select([f], [f], [f], 0)
    assert r == w == x == [f]
    del r, w, x
    # Now break things by mutating the list
    a.append(f)
    # This used to segfault, see http://bugs.python.org/issue2897
    r, w, x = select.select([f], [f], [f], 0)
    assert r == w == x == [f]

def test_select_errors():
    # Issue #3424: select() must raise a ValueError when passed a closed
    # file descriptor. Thanks to Martin von Loewis for the patch.
    fd = os.open(support.TESTFN, os.O_CREAT | os.O_WRONLY)
    try:
        os.close(fd)
        for args in [[[fd]], [[]], [[], [], [fd]]]:
            try:
                select.select(*args)
            except ValueError as e:
                assert
