import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    def callback(x):
        a.append(x)

    s = select.select([F()], [], [], 0)
    assert s == ([], [], [])
    s = select.select([F()], [], [], 0)
    assert s == ([], [], [])
    s = select.select([F()], [], [], 0)
    assert s == ([], [], [])
    s = select.select([F()], [], [], 0)
    assert s == ([], [], [])
    s = select.select([F()], [], [], 0)
    assert s == ([], [], [])
    s = select.select([F()], [], [], 0)
    assert s == ([], [], [])
    s = select.select([F()], [], [], 0)
    assert s == ([], [], [])
    s = select.select([F()], [], [], 0)
    assert s == ([], [], [])
