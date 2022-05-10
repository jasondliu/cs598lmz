import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
    a.append(F())

    # test that select doesn't mutate the list
    select.select([], a, [])
    assert a == [F()]

def test_error_conditions():
    # try:
    #     select.select([], [], [], "foo")
    # except TypeError:
    #     pass
    # else:
    #     assert False, 'timeout is not a float'

    # try:
    #     select.select([], [], [], None)
    # except TypeError:
    #     pass
    # else:
    #     assert False, 'timeout is not a float or None'

    # try:
    #     select.select([], [], [], -1.0)
    # except ValueError:
    #     pass
    # else:
    #     assert False, 'negative timeout'

    try:
        select.select([], [], [], 10.0)
    except ValueError:
        pass
    else:
        assert False, 'timeout too big'
