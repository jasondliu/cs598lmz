import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    try:
        select.select([F()], [], [], 5)
    except ValueError:
        return True
    except IndexError:
        return False
    else:
        raise AssertionError("didn't crash")

if not test_select_mutated():
    raise AssertionError("Didn't crash")
