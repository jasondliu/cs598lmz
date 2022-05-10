import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
    f = F()
    a.append(f)
    select.select(a, a, a)
    class G:
        def fileno(self):
            return 2
    g = G()
    a.append(g)
    select.select(a, a, a)


@banana
def test_empty():
    b"str"
    # this one must work until unicode is fixed
    "str"
    # the following ones must fail
    u"str"
    b"a" + b"b"
    b"a" + u"b"
    u"a" + u"b"
    b"a" + "b"
    "a" + u"b"
    s = u"a" + b"b"
    s = b"a" + s
    chr(1)
    unichr(2)
    list(b"str")
    list(u"str")
    [1, 2, 3][1:1]
    {(1, 2): 3}[(1,
