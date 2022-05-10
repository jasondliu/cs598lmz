import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    try:
        select.select([F()], [], [])
    except TypeError as e:
        assert e.args[0] == 'fileno() returned a number, but not a valid fd'

def test_error_with_select_operations():
    try:
        select.select([], [], [], 'foo')
    except TypeError as e:
        assert e.args[0] == 'integer argument expected, got str'
    else:
        assert False, 'TypeError not raised'

def test_select_with_non_numerical_fds():
    try:
        select.select([b'foo'], [], [])
    except TypeError as e:
        assert e.args[0] == 'argument must be an int, or have a fileno() method.'
    else:
        assert False, 'TypeError not raised'

def test_select_with_non_sequence():
    try:
        select.select(1, 2, 3)
    except TypeError as e:
        assert e.args[0] ==
