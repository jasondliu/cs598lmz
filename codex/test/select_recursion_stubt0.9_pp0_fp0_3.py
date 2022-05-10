import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
        def close(self):
            test_select_mutated()
            pass

    f = F()
    a.append(f)
    f.close()

    # This used to fail with a TypeError on calling fileno() and with a
    # NameError on deleting 'a'.
    select.select([f], [], [])

def test_select_bad_rdlist():
    try:
        select.select([0], [], [])
    except TypeError:
        pass
