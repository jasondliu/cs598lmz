import weakref
# Test weakref.ref() with a class that has a __del__ method.

class Foo:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print("Foo.__del__", self.name)

def callback(r):
    print("callback", r)

a = Foo("a")
r = weakref.ref(a, callback)
print("created", r)
print("created", weakref.getweakrefcount(a), weakref.getweakrefs(a))
print("created", r())
del a
print("deleted", r())
print("deleted", weakref.getweakrefcount(r()), weakref.getweakrefs(r()))
