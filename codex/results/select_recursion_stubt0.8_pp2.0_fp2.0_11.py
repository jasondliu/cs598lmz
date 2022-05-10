import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
    try:
        assert select.select([F()], [], [], 0) == ([], [], [])
    except ValueError:
        pass
    assert a

def test_select_check_list_param():
    with raises(TypeError):
        select.select(1, 2, 3, 4)

def test_select_check_timeout_param():
    with raises(TypeError):
        select.select([], [], [], 'spam')
