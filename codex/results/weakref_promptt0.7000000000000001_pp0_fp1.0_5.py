import weakref
# Test weakref.ref
class A(object):
    pass
a1 = A()
a2 = A()
a3 = A()
def foo(obj):
    print obj() # print weakref.ref object's object instance
f1 = weakref.ref(a1, foo)
f2 = weakref.ref(a2, foo)
f3 = weakref.ref(a3, foo)
del a1
del a2
del a3

# Test weakref.proxy
class A(object):
    pass
a1 = A()
a2 = A()
a3 = A()
def foo(obj):
    print obj # print weakref.proxy object's object instance
f1 = weakref.proxy(a1, foo)
f2 = weakref.proxy(a2, foo)
f3 = weakref.proxy(a3, foo)
del a1
del a2
del a3
