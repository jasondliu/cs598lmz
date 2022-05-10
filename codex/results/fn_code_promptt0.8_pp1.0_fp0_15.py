fn = lambda: None
# Test fn.__code__ and fn.__closure__ are set correctly
def test_closure_code():
    def fn():
        a = 20
        return a
    def fn2(fn):
        return fn()
    assert fn2(fn) == 20

# Test that we can get a cell, and that we can get the value from a cell
# Also tests that fn.__closure__ is a tuple, as it should be
def test_cell_and_cell_contents():
    a = 20
    def fn():
        return a
    assert fn.__closure__[0].cell_contents == 20

# Test custom function: add
def test_add():
    assert add(1, 2) == 3

# Test builtin function: abs
def test_abs():
    assert abs(-5) == 5
    assert abs(5) == 5
    assert abs(0) == 0

# Test builtin function: sum
def test_sum():
    assert sum([1, 2, 3]) == 6
    assert sum([]) == 0

# Test builtin function: all
def test_all():
