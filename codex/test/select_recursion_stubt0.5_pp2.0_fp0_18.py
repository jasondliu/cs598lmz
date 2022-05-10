import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(self)
            return 42

    f = F()
    select.select([f], [f], [f], 0.1)
    assert a == [f]


def test_select_interrupted():
    # Issue #11649
    class F:
        def fileno(self):
            return 42

    f = F()
    with pytest.raises(select.error) as excinfo:
        select.select([f], [f], [f], 0.1)
    assert excinfo.value.args == (4, 'Interrupted system call')


def test_select_timeout():
    # Issue #11649
    class F:
        def fileno(self):
            return 42

    f = F()
    with pytest.raises(select.error) as excinfo:
        select.select([f], [f], [f], -1)
    assert excinfo.value.args == (22, 'Invalid argument')


