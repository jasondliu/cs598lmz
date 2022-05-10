import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42

    a.append(F())

    fd = F()

    try:
        select.select([fd], a, a)
    except ValueError:
        pass

def test_select_bad_file():
    fd = object()
    try:
        select.select([fd], [], [])
    except ValueError:
        pass

def test_select_negative_timeout():
    select.select([], [], [], -1.0)

if __name__ == '__main__':
    test_select_mutated()
    test_select_bad_file()
    test_select_negative_timeout()
