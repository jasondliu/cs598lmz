import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 12

    class G:
        def fileno(self):
            a.append(2)
            return 15

    s = [F(), G()]
    try:
        select.select([], [], s, 0)
    except ValueError:
        pass
    assert len(a) == 1, a
    assert a[0] == 1, a
