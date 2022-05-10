import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

            return 0

    with pytest.raises(RuntimeError):
        select.select([F()], a, a)
