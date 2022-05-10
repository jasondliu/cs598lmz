import weakref
# Test weakref.ref(instance)

class MyClass:
    def __init__(self, name):
        self.name = name

obj = MyClass('MyObject')
r = weakref.ref(obj)
print(r)
print(r())
print(r().name)

obj2 = MyClass('MyObject2')
r2 = weakref.ref(obj2)
print(r2)
print(r2())
print(r2().name)

obj = None
print(r)
print(r())
print(r().name)

obj2 = None
print(r2)
print(r2())
print(r2().name)

r3 = weakref.ref(MyClass('MyObject3'))
print(r3)
print(r3())
print(r3().name)

r3 = None
print(r3)
print(r3())
print(r3().name)

# Test weakref.proxy(instance)
obj = MyClass('MyObject')
p = weakref.proxy(obj)
print(p)
