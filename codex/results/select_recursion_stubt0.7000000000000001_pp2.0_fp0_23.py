import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def do_not_call(self):
            a.append(1)
            return 5

    f = F()

    # Selecting on a mutated object should raise
    # ValueError
    with raises(ValueError):
        select.select([f], [], [])

    # Selecting on a mutated object should raise
    # ValueError
    with raises(ValueError):
        select.select([f], [], [], 0)

    # The object should have been mutated though
    assert a == [1]


class TestSelect:
    def test_error_conditions(self):
        # select() should throw a ValueError if given
        # an empty list
        with raises(ValueError):
            select.select([], [], [], 0)

        # select() should raise a ValueError if one of
        # the file descriptors is negative
        with raises(ValueError):
            select.select([-1], [], [], 0)

        # select() should raise a ValueError if one of
        # the file descriptors is greater or equal to FD_SET
