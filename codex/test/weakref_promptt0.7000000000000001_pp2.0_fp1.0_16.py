import weakref
# Test weakref.ref(...)
import weakref


class MyClass:
    def __init__(self):
        self.name = "John"


obj = MyClass()
ref = weakref.ref(obj)
print(ref.__class__)
print(ref.__sizeof__())
print(ref.__sizeof__()/2**10)

ref2 = weakref.ref(obj)
print(ref2.__class__)
print(ref2.__sizeof__())
print(ref2.__sizeof__()/2**10)


class MyClass:
    def __init__(self):
        self.name = "John"


obj = MyClass()
ref = weakref.ref(obj)
print(ref(),ref.__class__)
print(ref(),ref.__sizeof__())
print(ref(),ref.__sizeof__()/2**10)

ref2 = weakref.ref(obj)
print(ref2(),ref2.__class__)
print(ref2(),ref2.__sizeof__())
