import weakref
# Test weakref.ref()

class Foo:
    def __init__(self, name):
        self.name = name
        print("Created", self.name)
    def __del__(self):
        print("Deleted", self.name)

a = Foo("a")
r = weakref.ref(a)
print(r)
print(r())
print(r() is a)
del a
print(r())

print("-" * 20)

class Car:
    def __init__(self, name):
        self.name = name
        print("Created", self.name)
    def __del__(self):
        print("Deleted", self.name)

b = Car("b")
r = weakref.ref(b)
print(r)
print(r())
print(r() is b)
del b
print(r())
