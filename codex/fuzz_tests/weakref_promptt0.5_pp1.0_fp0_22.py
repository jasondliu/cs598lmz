import weakref
# Test weakref.ref()
def f():
    return 42
o = f()
r = weakref.ref(o)

# Test weakref.proxy()
o = f()
p = weakref.proxy(o)

# Test weakref.getweakrefcount()
o = f()
weakref.getweakrefcount(o)

# Test weakref.getweakrefs()
o = f()
weakref.getweakrefs(o)
