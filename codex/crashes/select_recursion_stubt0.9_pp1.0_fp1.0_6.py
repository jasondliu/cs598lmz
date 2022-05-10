import select
def test_select_mutated():
    class F:
        def fileno(self):
            test_select_mutated()
    f = F()
    try:
        select.select([f], [], [])
    except ValueError as ex:
        assert str(ex) == "I/O operation on closed file."
if __name__ == "__main__":
    test_select_mutated()
