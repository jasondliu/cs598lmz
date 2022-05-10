import select
def test_select_mutated():
    class F:
        def fileno(self):
            test_select_mutated()
    f = F()
    select.select([f], [f], [f])
if __name__ == "__main__":
    test_select_mutated()
