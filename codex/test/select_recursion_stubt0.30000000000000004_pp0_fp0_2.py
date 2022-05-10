import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())

    try:
        select.select([], a, [])
    except RuntimeError:
        pass

def test_select_large_fd():
    # Issue #11406: select() should not raise an exception for large file
    # descriptors.
    try:
        select.select([], [], [], 0)
    except ValueError:
        pytest.skip("select.select() failed")
    try:
        select.select([], [], [], 0, 1<<31)
    except ValueError:
        pytest.skip("select.select() failed")
    try:
        select.select([], [], [], 0, 1<<63)
    except ValueError:
        pytest.skip("select.select() failed")

