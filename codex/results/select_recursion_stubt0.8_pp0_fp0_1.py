import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]
    
    for i in range(100):
        a.append(F())
        select.select([a[-1]], [], [], 0)


def test_select_unknown():
    # Test with unknown file descriptor
    try:
        select.select([None], [], [], 0.1)
    except Exception as e:
        pass


if __name__ == '__main__':
    test_select_mutated()
    test_select_unknown()
