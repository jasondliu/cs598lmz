import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
        def close(self):
            a.append("close")

    s = select.select([F()], [], [], 1)
    if len(s) == 1:
        s[0][0].close()

    print("a =", a)
    assert a == ["close"]

test_select_mutated()
test_select_mutated()
