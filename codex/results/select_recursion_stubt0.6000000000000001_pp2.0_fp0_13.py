import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    r, w, x = select.select([F()], [], [])
    r, w, x = select.select([], [F()], [])
    r, w, x = select.select([], [], [F()])

    r, w, x = select.select([F()], a, a)
    r, w, x = select.select(a, [F()], a)
    r, w, x = select.select(a, a, [F()])

def test_select_bad_fd():
    r, w, x = select.select([1], [2], [3])

def test_select_bad_fd_in_list():
    r, w, x = select.select([1, 2], [3, 4], [5, 6])

def test_select_bad_fd_in_list_with_good_fd():
    r, w, x = select.select([1, 2], [3, 4], [5, 6])

def test_select_bad_fd_in_list_with
