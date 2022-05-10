import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 5

    with pytest.raises(ValueError):
        select.select([],[],[F()])

    a.append(1)
