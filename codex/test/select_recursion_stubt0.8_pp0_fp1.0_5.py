import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([], [F()], [])

def test_select_kwargs():
    select.select(timeout=1.0)
    select.select([], [], [], timeout=1.0)
    select.select(timeout=1.0, _track_allocations=True)
    select.select([], [], [], timeout=1.0, _track_allocations=True)

def test_select_tracking():
    result = select.select([], [], [], _track_allocations=True)
    assert result[0]._allocs == 0
    assert result[1]._allocs == 1
    assert result[2]._allocs == 1
    result[2]._allocs = -1
    result2 = select.select([], result[1], result[2], _track_allocations=True)
    assert result2[0]._allocs == 0
    assert result2[1]._allocs == 0
    assert result2[2]._allocs == -1

