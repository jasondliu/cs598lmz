import weakref
# Test weakref.ref(obj) equals weakref.proxy(obj)
def func(obj):
    wr = weakref.ref(obj)
    wp = weakref.proxy(obj)
    eq_(wr.__call__, wp.__call__)
    eq_(wr.__repr__, wp.__repr__)
    eq_(wr.__str__, wp.__str__)
    eq_(wr.__hash__, wp.__hash__)
    eq_(wr.__getattribute__, wp.__getattribute__)
    eq_(wr, wp)
    eq_(repr(wr), repr(wp))
    eq_(wr._obj, wp._obj)
    eq_(wr(), wp())  #bound method
    eq_(wr(), 10)  #func
    eq_(wr(), obj)  #class instance
    eq_(wr(), 'abc')  #str
    eq_(wr(), 4.2)  #float
    

class TestWeakref:

    def test_basic(self):
        class Foo: pass
        obj = Foo()
