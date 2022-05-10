import select
def test_select_mutated():
    class F:
        def fileno(self):
            test_select_mutated()
    f = F()
    select.select([f], [], [], 0)
def main():
    test_select_mutated()
main()
