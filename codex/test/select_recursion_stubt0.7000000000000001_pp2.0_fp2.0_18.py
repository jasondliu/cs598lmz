import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -10
        def close(self):
            a.append('close')

    f = F()
    try:
        select.select([], [f], [], 0)
    except ValueError:
        pass
    assert a == ['close']
