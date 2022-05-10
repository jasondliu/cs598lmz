import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42

        def close(self):
            a[:] = [1]

    def l(x):
        return (x for x in [F()])

    with pytest.raises(RuntimeError):
        select.select(l(1), l(2), l(3))

    assert not a

    with pytest.raises(RuntimeError):
        select.select(l(1), l(2))

    assert a == [1]

def foo():
    pass

def test_invalid_return():
    a = []
    pytest.raises(TypeError, select.select, [a], [], [], 1)
    assert not a, "must not call fileno of unhashable item"
