import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    class G:
        def fileno(self):
            del a[:]
            return 2

    a[:] = [F(), G()]

    for i in range(5):
        r, w, x = select.select(a, [], [])
        assert r == [a[0]], i

@pytest.mark.xfail(reason="https://bugs.python.org/issue34375")
def test_select_mutated_again():
    class F:
        def fileno(self):
            del a[:]
            return 1

    a = [F()]
    for i in range(5):
        r, w, x = select.select(a, [], [])
        assert r == [a[0]], i
