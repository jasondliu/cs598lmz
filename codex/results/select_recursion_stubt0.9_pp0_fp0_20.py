import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
    a.append(F())

    select.select([], a, [])

if __name__ == '__main__':
    test_select_mutated()
    print 'OK'
