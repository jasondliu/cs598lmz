import gc, weakref

def leaker():
    return []

def test_weakrefs():
    s = l = e = None
    def callback(wr):
        nonlocal l, e
        l = list(s)
        e = wr()
    s = { 'hello': 123 }
    wr = weakref.ref(s, callback)
    del s
    gc.collect()
    assert l == [('hello', 123)], l
    assert e is None
    s = l = e = None
    s = { 'abc': {}, 'def': {} }
    wr = weakref.ref(s['def'], callback)
    del s['def']
    gc.collect()
    assert l == [], l
    assert e is None
    s = l = e = None
    s = { 1: [2], 3: [4] }
    w = weakref.ref(s, callback)
    del s[1][0]
    gc.collect()
    assert l == [], l


class User:
    pass

