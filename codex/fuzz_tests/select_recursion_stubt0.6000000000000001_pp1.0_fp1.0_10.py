import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    select.select([F()], [], [])

def test_select_error_in_fileno():
    e = Exception()
    class F:
        def fileno(self):
            raise e
    try:
        select.select([F()], [], [])
    except Exception as e1:
        assert e1 is e


if __name__ == "__main__":
    test_select_mutated()
    test_select_error_in_fileno()
