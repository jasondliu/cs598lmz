import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 3

    a.append(F())
    try:
        select.select([], [a[0]], [], 0)
    except RuntimeError as e:
        assert "changed size during iteration" in str(e)
    else:
        assert 0, "did not catch RuntimeError"

def test_select_mutated_2():
    # This used to crash in 3.2 and 3.3 when the "a" list was not
    # copied with a slice, so it is worth testing again.  (The
    # previous test used a tuple instead of a list, which triggered
    # different code paths.)
    a = []

    class F:
        def fileno(self):
            a.clear()
            return 3

    a.append(F())
    try:
        select.select([], a, [], 0)
    except RuntimeError as e:
        assert "changed size during iteration" in str(e)
    else:
        assert 0, "did not catch RuntimeError"

def test_select_mutated_3():
    # Issue #159
