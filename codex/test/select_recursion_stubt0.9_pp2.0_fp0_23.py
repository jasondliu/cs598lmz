import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 5
        #def fileno():
        #    return 2
    x = select.select([F()], [], [])
    a.append(x)


if __name__ == '__main__':
    test_select_mutated()
