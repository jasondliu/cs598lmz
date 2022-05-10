import weakref
# Test weakref.ref() with a class that defines a __del__ method.

class A:
    def __init__(self):
        self.x = 1

    def __del__(self):
        print("del")

a = A()
r = weakref.ref(a)
print(r())
del a
print(r())

# Test weakref.ref() with a class that defines a __del__ method, and
# also a __weakref__ slot.

class B:
    def __init__(self):
        self.x = 1

    def __del__(self):
        print("del")

b = B()
b.__weakref__ = 1
r = weakref.ref(b)
print(r())
del b
print(r())

# Test weakref.ref() with a class that defines a __del__ method, and
# also a __weakref__ slot, but the slot is not a list.

class C:
    def __init__(self):
        self.x = 1

