import select
def test_select_mutated():
    a = []
    class F:
        def fileno(self):
            test_select_mutated()
    select.select([], [F()], a, 1)
if __name__ == "__main__":
    test_select_mutated()
