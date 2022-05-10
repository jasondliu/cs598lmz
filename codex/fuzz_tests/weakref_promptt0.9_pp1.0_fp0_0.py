import weakref
# Test weakref.reference.__new__.
import weakref

class DummyReference(weakref.ref):


    def __init__(self, ob, callback=None):
        weakref.ref.__init__(self, ob, callback)



class Foo(object):
    pass

a = Foo()
key = id(a)
a.attr = 12
b = DummyReference(a)


def callback(a):
    global key
    key = 0

del a
b(callback)
c = b()
c.attr
key
# Test weakref.proxy.
#
# See also test_descr.py for WeakKeyDictionary and WeakValueDictionary.  They
# use __hash__, __eq__ and __repr__, so this is the only place where we can
# test *all* aspects of warning generation.
import weakref

c = weakref.WeakKeyDictionary()

class C(object):


    def __hash__(self):
        pass



class D(object):


    def __hash__(self):
        return
