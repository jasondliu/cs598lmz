import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    a.append(F())
    try:
        select.select(a, [], [])
    except ValueError:
        pass
    else:
        fail("Expected ValueError")

def test_select_with_str():
    a = []

    class F:
        def fileno(self):
            return -1

    a.append(F())
    a.append("test")
    try:
        select.select(a, [], [])
    except TypeError:
        pass
    else:
        fail("Expected TypeError")

def test_rlist_rlist():
    rlist = rlist("abc")
    try:
        select.select(rlist, rlist, rlist)
    except TypeError:
        pass
    else:
        fail("Expected type error.")

def test_wlist_wlist():
    wlist = wlist("abc")
    try:
        select.select(wlist, wlist, wlist)
    except TypeError:
        pass
    else:

