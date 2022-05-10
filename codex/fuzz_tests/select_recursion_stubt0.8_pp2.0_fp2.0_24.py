import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    assert_raises(ValueError, select.select, [F()], [], [], 0)[0]

if __name__ == "__main__":
    test_select_mutated()
