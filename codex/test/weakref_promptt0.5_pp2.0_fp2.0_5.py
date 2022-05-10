import weakref
# Test weakref.ref() and weakref.proxy()

# weakref.ref()

class A:
    pass

a = A()
wr = weakref.ref(a)
print(wr)
print(wr())
print(type(wr))
print(wr.__class__)
print(wr())
print(wr() is a)

# weakref.proxy()

class A:
    pass

a = A()
wr = weakref.proxy(a)
print(wr)
print(wr())
print(type(wr))
print(wr.__class__)
print(wr())
print(wr() is a)

# weakref.WeakMethod()

class A:
    def foo(self):
        print('foo')

a = A()
am = weakref.WeakMethod(a.foo)
print(am)
print(am())
print(type(am))
print(am.__class__)
print(am())
print(am() is a)
print(am() is a.foo)

# weakref.WeakKeyDictionary()
