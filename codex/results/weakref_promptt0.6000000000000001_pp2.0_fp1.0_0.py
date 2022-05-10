import weakref
# Test weakref.ref and weakref.proxy with objects that implement the
# __slots__ attribute.

class C(object):
    __slots__ = ('a', 'b')

def test_basic(a=1, b=2):
    x = C()
    x.a, x.b = a, b
    p = weakref.proxy(x)
    x_ref = weakref.ref(x)
    x_ref() is x
    p.a is a
    p.b is b
    del x_ref
    del x
    try:
        p.a
    except ReferenceError:
        pass
    else:
        print('ReferenceError not raised')

def test_weakkeydict(a=1, b=2):
    x = C()
    x.a, x.b = a, b
    d = weakref.WeakKeyDictionary()
    d[x] = 42
    x_ref = weakref.ref(x)
    x_ref() is x
    del x
    try:
        d[x_ref()]
   
