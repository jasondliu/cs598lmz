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

o = o2 = None
print(r())
print(r2())

# Test weakref.ref() with a function

def f():
    pass

r = weakref.ref(f)
print(r)
print(r())

# Test weakref.ref() with a builtin function

r = weakref.ref(len)
print(r)
print(r())

# Test weakref.ref() with a builtin method

r = weakref.ref(''.join)
print(r)
print(r())

# Test weakref.ref() with a class method

class C:
    def f(self):
        pass

r = weakref.ref(C.f)
print(r)
print(r())

#
