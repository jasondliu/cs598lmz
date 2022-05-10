import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    with assert_raises(RuntimeError) as cm:
        select.select([], [F()], [])

    tb = cm.exconly()
    assert lines_fields([
        '* RuntimeError: tracemalloc_domain.py", line 91, in _add_frame',
    ], tb)

    with assert_raises(RuntimeError) as cm:
        select.select([], [], [F()])

    tb = cm.exconly()
    assert lines_fields([
        '* RuntimeError: tracemalloc_domain.py", line 91, in _add_frame',
    ], tb)
