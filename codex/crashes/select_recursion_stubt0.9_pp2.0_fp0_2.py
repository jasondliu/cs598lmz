import select
def test_select_mutated():
    class F:
        def fileno(self):
            test_select_mutated()
    try:
        select.select([], [F()], [])
    except:
        return
def main():
    test_select_mutated()
if __name__ == "__main__":
    main()
