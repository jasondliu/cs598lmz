import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    class G:
        def fileno(self):
            a.append(1)
            return 0

    select.select([F()], [G()], [], 10)


def test_select_error():
    # Issue #5855
    assert select.select([], [], [], 10) == ([], [], [])
    try:
        select.select([], [], [], 'x')
    except TypeError:
        pass
    else:
        pytest.fail("expected TypeError")
