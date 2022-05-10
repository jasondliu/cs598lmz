import weakref
# Test weakref.ref(self)

class C:
    pass

def f(x):
    print(x)

c = C()
r = weakref.ref(c, f)
print(r)
print(r())

# Test weakref.ref(self, callback)

class C:
    pass

def f(x):
    print(x)

c = C()
r = weakref.ref(c, f)
print(r)
print(r())

# Test weakref.ref(self, callback, ...)

class C:
    pass

def f(x):
    print(x)

c = C()
r = weakref.ref(c, f, "a", "b", "c")
print(r)
print(r())

# Test weakref.ref(self, callback, ...)

class C:
    pass

def f(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)

c = C()
