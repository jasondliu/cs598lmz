import weakref
# Test weakref.ref()
print 'weakref.ref(object):', weakref.ref(object)
print 'weakref.ref(int):', weakref.ref(int)

print 'weakref.ref(object, callback):', weakref.ref(object, lambda x, y: x + y)
print 'weakref.ref(int, callback):', weakref.ref(int, lambda x, y: x + y)

# Test weakref.proxy()
print 'weakref.proxy(object):', weakref.proxy(object)
print 'weakref.proxy(int):', weakref.proxy(int)

# Test weakref.getweakrefcount()
print 'weakref.getweakrefcount(object):', weakref.getweakrefcount(object)
print 'weakref.getweakrefcount(int):', weakref.getweakrefcount(int)

# Test weakref.getweakrefs()
print 'weakref.getweakrefs(object):', weakref.getweakrefs(object)
print 'weakref.getweakrefs(int):', weakref.get
