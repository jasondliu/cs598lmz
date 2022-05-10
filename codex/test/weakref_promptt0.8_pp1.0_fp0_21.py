import weakref
# Test weakref.ref() and weakref.proxy()

a = 1
ref = weakref.ref(a)
print("ref = weakref.ref(a)")
print("ref is", ref)
print("ref.__class__ is", ref.__class__)
print("ref() is", ref())
print("ref() == a is", ref() == a)
print()

b = a
proxy = weakref.proxy(b)
print("proxy = weakref.proxy(a)")
print("proxy is", proxy)
print("proxy.__class__ is", proxy.__class__)
print("proxy == a is", proxy == a)
print("proxy is a is", proxy is a)
print("proxy is b is", proxy is b)
print("proxy + 1 is", proxy + 1)

def cb(proxy):
    print("cb running")
proxy_cb = weakref.proxy(a, cb)

def cb_cb(cb):
    print("cb_cb running")
    print(cb)
