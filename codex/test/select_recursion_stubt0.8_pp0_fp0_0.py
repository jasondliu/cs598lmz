import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    a.append(F())

    fs = select.select([a[0]], [], [])
    assert list(fs[0]) == a, fs
    assert list(fs[1]) == [], fs
    assert list(fs[2]) == [], fs
