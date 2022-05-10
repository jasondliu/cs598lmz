import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    def f(r):
        assert r == [F()]
        a.append(1)
        return [F()]

    select.select(f([F()]), [], [])

def test_select_str_fileno():
    class F:
        def __str__(self):
            return 'hi'

    with raises(TypeError):
        select.select([F()], [], [], 1)
