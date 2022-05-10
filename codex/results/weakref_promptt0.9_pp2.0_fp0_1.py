import weakref
# Test weakref.ref(ProxyType)
weakref.ref(weakref.ProxyType)
# Test weakref.proxy(ProxyType)
proxy = weakref.proxy(weakref.ProxyType)
proxy
repr(proxy)
print(proxy)
# Test weakref.ref(callable)
weakref.ref(object.__init__)
# Test weakref.proxy(callable)
proxy = weakref.proxy(object.__init__)
proxy
repr(proxy)
print(proxy)

# Verify that calling a different instance method does not trigger an error
proxy(weakref.ProxyType)
