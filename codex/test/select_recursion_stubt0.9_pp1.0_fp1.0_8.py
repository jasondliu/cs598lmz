import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([F()], [], [])
    select.select([F()], [], [], 0.0)
    a.append(1)


def test_select_largefdset():
    s = []
    for i in range(100000):
        s.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

    select.select(s, [], [])
    select.select(s, [], [], 0.0)


def main():
    test_select_mutated()
    test_select_largefdset()

if __name__ == '__main__':
    main()
