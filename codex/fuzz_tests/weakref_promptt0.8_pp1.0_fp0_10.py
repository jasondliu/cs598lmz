import weakref
# Test weakref.ref.__new__ with a custom class.
#


class Ref(weakref.ref):
    pass


def callback(r, lst):
    lst.append(r)


def iseq(it1, it2):
    for x, y in zip(it1, it2):
        if x is not y:
            return False
    return True


def test_callback():
    lst = []
    o = object()
    o_wr = Ref(o, callback, (lst,))
    o1_wr = Ref(o, callback, (lst,))
    o2_wr = Ref(object(), callback, (lst,))
    assert lst == []
    del o2_wr
    assert lst == []
    del o
    assert lst == [o_wr, o1_wr]
    del o1_wr
    assert lst == [o_wr, o1_wr]
    del o_wr
    assert lst == [o_wr, o1_wr]
    del lst
    assert o_wr
