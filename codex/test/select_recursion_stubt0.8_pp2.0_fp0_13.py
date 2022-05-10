import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1

    class G:
        def fileno(self):
            a.append(2)
            return 2

    s = select.select([G(), F()], [], [], 1)
    assert a == [1, 2]
