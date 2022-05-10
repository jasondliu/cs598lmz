import weakref
# Test weakref.ref
r = weakref.ref(lambda: None)
r()
r
r()
r
# Test weakref.WeakKeyDictionary
a = weakref.WeakKeyDictionary()
a[1] = 1
a
a[2] = 2
a
del 2
a
# Test weakref.WeakValueDictionary
b = weakref.WeakValueDictionary()
b[1] = 1
b
b[2] = 2
b
del 2
b
# Test weakref.WeakSet
c = weakref.WeakSet()
c.add(1)
c
c.add(2)
c
del 2
c
# Test weakref.finalize
class C:
    pass

obj = C()
finalizer = weakref.finalize(obj, lambda: print('obj deleted'))
finalizer.alive
obj = None
finalizer.alive
# Test weakref.WeakMethod
class C:
    def f(self):
        pass

obj = C()
r = weakref.WeakMethod(obj.f)
r()
r
r
