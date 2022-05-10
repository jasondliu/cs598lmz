import weakref
# Test weakref.ref

import weakref

class A:
    pass

class B(A):
    pass

class C(A):
    pass

def test_ref(ref):
    print(ref())
    print(ref.alive)


a = A()
b = B()
c = C()

test_ref(weakref.ref(a))
test_ref(weakref.ref(b))
test_ref(weakref.ref(c))

print(weakref.getweakrefcount(a))
print(weakref.getweakrefcount(b))
print(weakref.getweakrefcount(c))

print(weakref.getweakrefs(a))
print(weakref.getweakrefs(b))
print(weakref.getweakrefs(c))
