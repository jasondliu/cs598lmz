import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def read(self):
            a.append(1)

    select.select([F()], [F()], [], 0)



def test_select_closed_pipe():
    import select, os

    r, w = os.pipe()
    try:
        os.close(r)
        select.select([r], [], [], 0)
    except ValueError:
        pass

    try:
        os.close(w)
        select.select([], [w], [], 0)
    except ValueError:
        pass

# This test makes sure that the module attribute __doc__ is not None, even
# though it is not declared in the module.
def test_module___doc__():
    import select
    assert select.__doc__ is not None

def test_select_error():
    import select

    raises(select.error, "select.select([-1], [], [], 0)")
    raises(select.error, "select.select([], [-1], [], 0)")
    raises(select.
