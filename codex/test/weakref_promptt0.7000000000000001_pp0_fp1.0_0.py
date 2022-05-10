import weakref
# Test weakref.ref
class C:
    pass

class A:
    def __init__(self,b):
        self.b = b

a = A(C())
r = weakref.ref(a)
print(r)
print(r())
r().b
print(r().b is a.b)
a = None
print(r())

# Test weakref.WeakKeyDictionary
#
# Make sure that a WeakKeyDictionary doesn't keep objects alive
#
class A:
    pass

class B:
    pass

def f():
    a = A()
    b = B()
    d = weakref.WeakKeyDictionary({a: 1, b: 2})
    print(d)
    print(d[a])
    print(d[b])
    return d

d = f()
print(d)
print(d[A()])
print(d[B()])

# Test weakref.WeakValueDictionary
#
# Make sure that a WeakValueDictionary doesn't keep objects alive
#
class A:
    pass

