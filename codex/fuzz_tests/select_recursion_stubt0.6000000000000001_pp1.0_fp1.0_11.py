import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([F()], [], [], 0)

def test_select_strange_error():
    # Issue #6145: on Windows, select() should raise a ValueError if
    # the first parameter is an empty list
    try:
        select.select([], [], [], 0)
    except ValueError:
        pass
    else:
        raise Exception('Expected ValueError')
