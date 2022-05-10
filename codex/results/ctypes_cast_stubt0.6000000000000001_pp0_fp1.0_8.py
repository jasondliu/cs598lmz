import ctypes
ctypes.cast(1, ctypes.py_object)
id(None)
sys.getrefcount(1)
a = [1, 2, 3]
b = a
sys.getrefcount(a)
del a
sys.getrefcount(b)
import weakref
a = [1, 2, 3]
r = weakref.ref(a)
r()
del a
r()
r() is None
r() is None
r() is None
r() is None
r() is None
r() is None
r() is None
r() is None
r() is None
r() is None
r() is None
print(r())
import weakref
class ExpensiveObject(object):
    def __del__(self):
        print('(Deleting %s)' % self)
obj = ExpensiveObject()
r = weakref.ref(obj)
print('obj:', obj)
print('ref:', r)
print('r():', r())
print('deleting obj')
del obj
print('r():', r())
class ExpensiveObject(object):

