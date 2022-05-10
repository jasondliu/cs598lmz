import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append('fileno')

    with suppress(RuntimeError):
        select.select([F()], [], [])

    assert a == ['fileno']
