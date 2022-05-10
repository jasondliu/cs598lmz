import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(self)
            return 5

    select.select([F()], [F()], [F()], 100)

    assert a == [a[0], a[0], a[0]]

def test_unix_select():
    if not hasattr(select, "select"):
        skip("Requires select.select implementation")
    fd = os.open("/dev/null", os.O_RDONLY)
    r, w, x = select.select([fd], [fd], [fd], 0)
    assert r == [fd], "Wrong result from select.select"

    os.close(fd)

def test_unix_select_timeout():
    if not hasattr(select, "select"):
        skip("Requires select.select implementation")
    r, w, x = select.select([], [], [], 0.5)
    assert r == [] and w == [] and x == []

