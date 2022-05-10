import weakref
# Test weakref.ref() with a class instance.
import weakref

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

# Test weakref.ref() with a function.
def f():
    pass

r = weakref.ref(f)
print(r)
print(r())

# Test weakref.ref() with a builtin function.
import math

r = weakref.ref(math.sin)
print(r)
print(r())

# Test weakref.ref() with a builtin method.
r = weakref.ref('hello'.upper)
print(r)
print(r())

# Test weakref.ref() with an instance method.
class C:
    def f(self):
        pass

o = C()
r = weakref.ref(o.f)
print(r)
print(r())

# Test weakref.ref() with a class method.
class C:
    @classmethod
    def f(cls):
        pass


