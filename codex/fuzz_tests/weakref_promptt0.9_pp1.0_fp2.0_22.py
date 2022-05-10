import weakref
# Test weakref.ref() and weakref.WeakValueDictionary

class X:
    pass

x =  X()
x.attr = 42

def test_value_ref():

    d = weakref.WeakValueDictionary()
    d['a'] = x
    assert(d['a'].attr == 42)

    import gc
    x.attr = 24
    x = None
    gc.collect()

    assert(d['a'].attr == 24)
    return



def test_key_ref():

    class Key(object):

        def __init__(self, obj):
            self.obj = obj

        def __eq__(self, other):
            return id(self.obj) == id(other.obj)

        def __hash__(self):
            return hash(id(self.obj))

    d = weakref.WeakValueDictionary()
    d[Key(x)] = x
    assert(d[Key(x)].attr)

    import gc
    x.attr = 24
    x = None
    gc.collect()

    assert
