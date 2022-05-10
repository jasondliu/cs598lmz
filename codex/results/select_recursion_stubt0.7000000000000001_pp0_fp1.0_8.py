import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def close(self):
            a.append(1)

    s = select.select([F()], [], [])
    del s
    test_select_mutated()
    import gc; gc.collect()
    test_select_mutated()
    assert a == [1, 1]
    test_select_mutated()

def test_select_closed_file():
    import os, select
    fd = os.open(__file__, os.O_RDONLY)
    os.close(fd)
    assert select.select([fd], [], [])[0] == []


class TestSelect:
    def test_select(self):
        import select
        for i in [0, 1]:
            r, w, x = select.select([], [], [], 0)
            assert r == w == x == [], [r, w, x]
            r, w, x = select.select([], [], [])
            assert r == w == x == [], [r, w, x]
            r,
