import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())

    b = select.select([], [], a)
    #print('exit select')

if __name__ == '__main__':
    for _ in range(1000):
        test_select_mutated()
