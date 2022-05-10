import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
    a.append(F())
    test_select_mutated()

def test_select_all_empty_list():
    select.select([], [], [], 1)

def test_select_all_empty():
    select.select([], [], [], 1)

def test_select_all_empty_tuple():
    select.select((), (), (), 1)

def test_select_all_empty_bad_timeout():
    # this used to crash
    select.select([], [], [], 1.1)

def test_select_all_empty_bad_timeout_negative():
    try:
        select.select([], [], [], -1)
    except ValueError:
        pass
    else:
        assert False, 'Should have raised ValueError'

def test_select_all_empty_bad_timeout_too_large():
    try:
        select.select([], [], [], 1e200)
    except ValueError:
        pass
    else:
        assert False, 'Should have raised ValueError'

