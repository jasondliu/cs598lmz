import select
def test_select_mutated():
    class F:
        def fileno(self):
            test_select_mutated()
    select.select([F()], [F()], [F()], 0)
if __name__ == '__main__':
    test_select_mutated()
