import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    b = []
    if select.select([f], a, b, 0.0) != ([], [], []):
        raise RuntimeError("select mutated its arguments")

    f = F()
    if select.select([f], a, b, 0.0) != ([], [], []):
        raise RuntimeError("select mutated its arguments")

    if select.select([f], a, b, 0.0) != ([], [], []):
        raise RuntimeError("select mutated its arguments")

test_select_mutated()
