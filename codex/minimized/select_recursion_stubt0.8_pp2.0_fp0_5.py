import select
def test_select_mutated():
    a = []
    class F:
        def fileno(self):
            test_select_mutated()
    f = F()
    a.append(f)
    select.select([], [], a)
if __name__ == "__main__":
    test_select_mutated()
