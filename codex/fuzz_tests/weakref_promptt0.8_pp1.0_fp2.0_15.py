import weakref
# Test weakref.ref()

def test(testfunc):
    print testfunc.__doc__
    testfunc()
    print 'ok'

def f():
    pass

def g():
    pass

def del_f(*args):
    print args[1]

def del_g(*args):
    print args[1]

class Foo:
    pass

def test_weakref_ref():
    import weakref
    f = Foo()
    f.x = 1
    ref = weakref.ref(f, del_f)
    print ref().x
    del f
    print gc.collect()
    try:
        ref()
    except ReferenceError, e:
        print e
    else:
        raise TestFailed, 'ref() should raise ReferenceError'

def test_weakref_getweakrefcount():
    import weakref
    f = Foo()
    f.x = 1
    ref1 = weakref.ref(f, del_f)
    ref2 = weakref.ref(f, del_f)
    ref3 = weakref
