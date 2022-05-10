import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def callback():
        a.append(1)
        raise StopIteration

    try:
        select.select([F()], [], [], 0)
    except RuntimeError:
        pass

    try:
        select.select([], [F()], [], 0)
    except RuntimeError:
        pass

    try:
        select.select([], [], [F()], 0)
    except RuntimeError:
        pass

    try:
        select.select([], [], [], 0, F())
    except RuntimeError:
        pass

    try:
        select.select([], [], [], 0, callback=callback)
    except StopIteration:
        pass

    assert a == [1]
