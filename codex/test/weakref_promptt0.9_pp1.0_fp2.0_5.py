import weakref
# Test weakref.ref() and weakref.proxy() on function objects.


def cb(r, l):
    l.append(r())


def get_meth():
    return list.append, None


def check(l, t, wr):
    print(wr)
    if t == list:
        self = l
    else:
        self = NoMatch
    assert wr() is t
    assert wr()() is t()
    assert wr(1) is t(1)
    assert wr(1)(2) is t(1)(2)
    assert wr(t, 1) is t(t, 1)
    assert wr(t, 1)(2) is t(t, 1)(2)
    assert wr(self, 1) is t(self, 1)
    assert wr(self, 1)(2) is t(self, 1)(2)


def add(x, y):
    return x + y


def add_self(self, x, y):
    return x + y


def multi3(x):
    return x * 3


