import weakref
# Test weakref.ref(f) for function f.

# Test the basic functionality of weak references.

def f(): pass

def callback(reference):
    print 'callback called'
    r = reference()
    print 'callback: r=', r

def test_basic():
    r = weakref.ref(f, callback)
    print 'r=', r
    print 'f=', f
    print 'r():', r()
    print 'deleting f'
    del f
    print 'r():', r()
    print 'r=', r

# Test the basic functionality of a weak reference to an instance method.

class Foo:
    def f(self): pass

def test_basic_method():
    o = Foo()
    r = weakref.ref(o.f, callback)
    print 'r=', r
    print 'o=', o
    print 'r():', r()
    print 'deleting o'
    del o
    print 'r():', r()
    print 'r=', r

# Test the basic functionality of a weak reference to
