import weakref
# Test weakref.ref(obj)
class Foo(object):
    pass

f = Foo()

print(weakref.ref(f))

# Test weakref.WeakKeyDictionary(dict)

d = {"key1": 1, "key2": 2}

print(weakref.WeakKeyDictionary(d))

# Test weakref.WeakValueDictionary(dict)

d = {"value1": 1, "value2": 2}

print(weakref.WeakValueDictionary(d))

# Test weakref.getweakrefcount(object)

class Foo(object):
    pass

f = Foo()

print(weakref.getweakrefcount(f))

# Test weakref.getweakrefs(object)

class Foo(object):
    pass

f = Foo()

print(weakref.getweakrefs(f))

# Test weakref.proxy(object[, callback])
# Test weakref.ProxyTypes

class Foo(object):
    pass

f = Foo()

print(weakref.proxy(f))

