import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def read(self):
            return 1
    a.append(F())
    select.select([a[0]],[],[],1)

if __name__ == '__main__':
    test_select_mutated()
