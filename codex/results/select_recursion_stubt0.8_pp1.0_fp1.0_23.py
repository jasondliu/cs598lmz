import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    r = [F()]
    result = select.select(r, a, a, 1.0)
    assert result == ([], [], []), result

# Ensure that select does not throw an exception about closed file
# descriptors when passed closed files.

def test_select_closed():
    a = []
    r, w = os.pipe()
    os.close(r)
    os.close(w)
    result = select.select([r], a, a, 1.0)
    assert result == ([], [], []), result

def test_select_overflow():
    # Under PyPy, the value of 'FD_SETSIZE' is given by
    # Py_GETENV("FD_SETSIZE"), which takes precedence over the internal
    # 'posix_fd_setsize' variable.
    # When set, 'FD_SETSIZE' must be correctly parsed as an integer.
    # This test is for issue #17271 (pypy) and #17209 (cpython).
    with env_var("FD_SETSIZE", "
