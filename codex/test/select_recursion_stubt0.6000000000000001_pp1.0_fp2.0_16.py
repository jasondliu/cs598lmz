import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    class P:
        def poll(self):
            a.append(1)
            return 1, 0

    select.select([F()], [], [], 0.0)
    select.select([], [F()], [], 0.0)
    select.select([], [], [F()], 0.0)
    select.poll()
    p = P()
    select.select([p], [], [], 0.0)
    select.select([], [p], [], 0.0)
    select.select([], [], [p], 0.0)
    select.poll()
    if a:
        raise AssertionError


def test_main():
    test_select_mutated()

if __name__ == "__main__":
    test_main()
