import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

        def close(self):
            a.append(1)

    select.select([F()], [], [], 10)

    assert a == [1]
