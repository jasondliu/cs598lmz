import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()  # do not crash here
            return -1

    a.append(F())
    try:
        select.select([], [], [])
    except OSError:
        pass
    assert not a  # crash here

def test_select_error():
    try:
        select.select([-1], [], [])
    except OSError:
        pass
    else:
        raise AssertionError("should have raised")

def main():
    test_select_mutated()
    test_select_error()

main()
