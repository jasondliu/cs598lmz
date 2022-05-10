import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated(); return 0
    f = F()
    d = {f: a, 1: [2], 3: [4]}
    for i in range(200):
        print i
        r, w, x = select.select([], d, [], 0)
    print d

if __name__ == '__main__':
    test_select_mutated()
