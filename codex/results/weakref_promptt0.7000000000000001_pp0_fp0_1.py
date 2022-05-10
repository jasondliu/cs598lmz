import weakref
# Test weakref.ref to weakref.WeakKeyDictionary
# References to Foo should not prevent collection of Foo


class Foo(object):
    pass


def callback(wr):
    global called
    called = True


def callback1(wr):
    global called1
    called1 = True

called = False
called1 = False

f1 = Foo()
f2 = Foo()

f1.d = weakref.WeakKeyDictionary({f1: 1, f2: 2})
f1.d[f1] = 1
f1.d[f2] = 2

f2.d = weakref.WeakKeyDictionary()
f2.d[f1] = 1
f2.d[f2] = 2

wr = weakref.ref(f1, callback)
wr1 = weakref.ref(f1, callback1)
del f1
assert f2.d is not None
f2.d = None
assert called1
f2.d = 1
del f2
assert called
