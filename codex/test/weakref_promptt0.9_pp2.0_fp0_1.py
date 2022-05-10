import weakref
# Test weakref.ref(ProxyType)
weakref.ref(weakref.ProxyType)
# Test weakref.proxy(ProxyType)
proxy = weakref.proxy(weakref.ProxyType)
proxy
repr(proxy)
print(proxy)
# Test weakref.ref(callable)
