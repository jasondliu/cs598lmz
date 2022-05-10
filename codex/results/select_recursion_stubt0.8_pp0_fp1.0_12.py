import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a, 1)

def test_recursion_limit():
    import sys
    select.select([], [], [], 0)
    sys.setrecursionlimit(1)
    try:
        select.select([], [], [], 0)
    except RuntimeError:
        pass
    else:
        raise Exception("recursion limit not observed")
