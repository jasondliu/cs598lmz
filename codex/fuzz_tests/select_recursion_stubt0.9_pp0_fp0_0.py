import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 10

    a.append(F())
    try:
        select.select([F()], test_select_mutated, test_select_mutated, 1)
    except RuntimeError:
        print('test_select_mutated ok')
    else:
        print('test_select_mutated failed!')


def test_select_stress():
    r = []
    w = []

    # two passes over floats because the second pass often causes errors
    for _ in range(2):
        for i in float_range(10_000_000, 20_000_000):
            if i not in r and i not in w:
                r.append(i)
            if i not in w:
                w.append(i)

    # should not raise an exception
    select.select(r, w, test_select_mutated, 1)
    print('test_select_stress ok')


def main():
    test_select_mutated()
    test_select_stress()


if __name__ == '__main__':
    main()
