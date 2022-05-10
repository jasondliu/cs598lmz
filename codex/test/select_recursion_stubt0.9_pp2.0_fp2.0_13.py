import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(0)

    def next():
        if a:
            a.pop()
        raise StopIteration

    def test():
        iter(next, None)

    saved = select.select
    try:
        select.select = test
        select.select([F()], [], [])
    finally:
        select.select = saved
