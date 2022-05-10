import weakref
# Test weakref.ref() with a class instance.
import weakref

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(o)

# Test weakref.ref() with a function.
import weakref

def f():
    pass

r = weakref.ref(f)
print(r)
print(r())
print(f)

# Test weakref.ref() with a builtin function.
import weakref

r = weakref.ref(len)
print(r)
print(r())
print(len)

# Test weakref.ref() with a builtin method.
import weakref

r = weakref.ref(''.join)
print(r)
print(r())
print(''.join)

# Test weakref.ref() with a method.
import weakref

class C:
    def f(self):
        pass

o = C()
r = weakref.ref(o.f)
print(r)
print(r())
