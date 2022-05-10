import select
def test_select_mutated():
    class F:
        def fileno(self):
            test_select_mutated()
    select.select([], [], [F()], 0.0)
def test_main():
    test_select_mutated()
if __name__ == "__main__":
    test_main()
