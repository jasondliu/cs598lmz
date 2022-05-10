import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 100

        def close(self):
            pass

            @select.select([F()], [], [])
            def g(r, w, x):
                a.append(r)
                a.append(w)
                a.append(x)

    g()
    assert a == [[], [], []]
