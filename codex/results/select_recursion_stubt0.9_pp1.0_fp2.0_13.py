import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
        def close(self):
            a.append(1)

    try:
        r, w, e = select.select([F()], [], [], 0)
    except TypeError:
        pass

    if a:
        print('raised some other exception')

test_select_mutated()
