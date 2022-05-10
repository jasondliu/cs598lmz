import weakref
# Test weakref.ref() with a class instance

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2)
print(r2)
print(r2())

# Test weakref.ref() with a class instance method

class D:
    def f(self):
        pass

o = D()
r = weakref.ref(o.f)
print(r)
print(r())

o2 = D()
r2 = weakref.ref(o2.f)
print(r2)
print(r2())

# Test weakref.ref() with a builtin function

import builtins

r = weakref.ref(builtins.id)
print(r)
print(r())

r2 = weakref.ref(builtins.id)
print(r2)
print(r2())

# Test weakref.ref() with a builtin method

