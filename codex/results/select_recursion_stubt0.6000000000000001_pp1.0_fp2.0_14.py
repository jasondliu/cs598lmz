import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # this is not allowed
            a.append(1)
            return 1
    f = F()

    # segfault
    # select.select([f], [], [])
    # assert a == [1]

    # segfault
    # select.select([], [f], [])
    # assert a == [1]

    # segfault
    # select.select([], [], [f])
    # assert a == [1]

    # segfault
    # select.select([f], [f], [f])
    # assert a == [1]

    # segfault
    # select.select([f], [f], [f], 2)
    # assert a == [1]

    # segfault
    # select.select([f], [f], [f], 2, 2)
    # assert a == [1]
