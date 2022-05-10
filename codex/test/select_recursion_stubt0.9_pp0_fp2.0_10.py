import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()   # mutate 'a'

    class G:
        def fileno(self):
            return 3

    try:
        a.append(F())
        select.select([F()], a, a)
    except ValueError:
        pass
    else:
        # We should have thrown an error.
        raise AssertionError("didn't detect mutation of arglist")

    # However, when you mutate a list being iterated over but
    # don't change the list itself, no error should be thrown.
    x = True
    a.append(G())
    for fd in a:
        if x:
            a.append(G())
        x = False
        if hasattr(fd, 'fileno'):
            return
    raise AssertionError("didn't detect mutation of list being iterated over")

def test_error_conditions():
    # check various error conditions in poll/select
    try:
        select.poll()
    except SelectError:
        pass
