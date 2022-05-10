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
            return 1

    select.select([F()], [G()], [], 0)
    assert a
