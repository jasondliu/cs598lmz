import weakref
# Test weakref.ref(object)
import weakref

class A:
    pass

a = A()
a_ref = weakref.ref(a)
print(a_ref)

a_ref()

# Test weakref.proxy(object)
import weakref

class A:
    pass

a = A()
a_proxy = weakref.proxy(a)

print(a_proxy)

print(a_proxy.__class__)

a_proxy()

# Test weakref.getweakrefcount(object)
import weakref

class A:
    pass

a = A()
a_ref = weakref.ref(a)
print(weakref.getweakrefcount(a))

# Test weakref.getweakrefs(object)
import weakref

class A:
    pass

a = A()
a_ref = weakref.ref(a)
print(weakref.getweakrefs(a))

# Test weakref.finalize(object, callback, args, kwargs)
import weakref

