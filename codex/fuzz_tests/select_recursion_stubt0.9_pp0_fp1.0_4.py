import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 100

    assert select.select([a, F()], [a], [a]) == ([], [], [])

if __name__ == "__main__":
    test_select_mutated()
    test_select_mutated()
