import weakref
# Test weakref.ref(...)
# Test weakref.proxy(...)
# Test weakref.getweakrefcount(...)
# Test weakref.getweakrefs(...)
# Test weakref.ReferenceType
# Test weakref.ProxyType
# Test weakref.CallableProxyType
# Test weakref.ProxyTypes
# Test weakref.ref(object)
# Test weakref.ref(object, callback)

def callback(arg):
    global callback_called
    callback_called += 1
    if arg is not obj:
        raise TestFailed("Argument to callback is not the weak referenced object")

callback_called = 0
obj = C()
obj.a = 1
obj.b = 'hello'
obj.c = (1, 2, 3)
obj.d = [1, 2, 3]
obj.e = {'a':1, 'b':2}
obj.f = C()
obj.f.x = 1
obj.f.y = 2
obj.f.z = obj
r = weakref.ref(obj, callback)
if callback_called:
    raise
