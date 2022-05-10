import weakref
# Test weakref.ref()

class MyClass:
    pass

def callback(reference):
    print("callback(", reference, ")")

obj = MyClass()
r = weakref.ref(obj, callback)
print("obj:", obj)
print("ref:", r)
print("r():", r())
print("deleting obj")
del obj
print("r():", r())

print("\n")

# Test weakref.proxy()

obj = MyClass()
p = weakref.proxy(obj, callback)
print("obj:", obj)
print("proxy:", p)
print("deleting obj")
del obj
print("p.attr:", p.attr)

print("\n")

# Test weakref.getweakrefcount() and weakref.getweakrefs()

obj = MyClass()
p1 = weakref.proxy(obj)
p2 = weakref.proxy(obj)
print("obj:", obj)
print("proxy1:", p1)
print("proxy2:", p2)
print("refcount
