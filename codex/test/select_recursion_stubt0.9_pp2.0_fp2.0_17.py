import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 4
    select.select([F()], [], [], 0)
    select.select([], [F()], [], 0)
    select.select([], [], [F()], 0)

def test_recursion_limit():
    LE = (
        "RuntimeError: maximum recursion depth exceeded "
        "while calling a Python object"
    )
    def recurse(n):
        recurse(n + 1)

    old_limit = sys.getrecursionlimit()
    try:
        def test(limit):
            sys.setrecursionlimit(limit)
            try:
                recurse(0)
            except RuntimeError as e:
                if not str(e).startswith(LE):
                    raise
        with self.assertRaises((RecursionError, RuntimeError)):
            test(2)
        with self.assertRaises((RecursionError, RuntimeError)):
            test(4)
        test(6)
    finally:
        sys.setrecursionlimit(old_limit)

