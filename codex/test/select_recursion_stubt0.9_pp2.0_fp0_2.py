import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    try:
        select.select([], [F()], [])
    except:
        return

    for i in range(10):
        try:
            select.select([], a, [])
        except:
            pass


def main():
    test_select_mutated()

if __name__ == "__main__":
    main()
