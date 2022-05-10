import weakref
# Test weakref.ref.
print(weakref.ref(1))
print(weakref.ref(1))
print(weakref.ref(1))

# Test weakref.getweakrefcount.
print(weakref.getweakrefcount(1))

# Test weakref.getweakrefs.
print(weakref.getweakrefs(1))

# Test weakref.proxy.
print(weakref.proxy(1))

# Test weakref.finalize.
print(weakref.finalize(1, lambda *args: None))
