import weakref
# Test weakref.ref()
import weakref


class MyClass(object):
    pass


def fn(a):
    print(a)

obj = MyClass()
r1 = weakref.ref(obj)
r2 = weakref.ref(obj, fn)
r3 = weakref.ref(obj, fn)
print(r1())
print(r2())
print(r3())
del obj
print(r1())
print(r2())
print(r3())
