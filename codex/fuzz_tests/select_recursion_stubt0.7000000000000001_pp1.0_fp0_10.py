import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            while True:
                a.append(5)
                yield 5

    select.select([F()], [], [])
    assert a
