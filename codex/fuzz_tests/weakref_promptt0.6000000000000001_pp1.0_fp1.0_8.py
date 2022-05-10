import weakref
# Test weakref.ref() to a function

def f(x):
    return x**2

r = weakref.ref(f)
print(r)
print(r())
print(r()(2))

print(r() is f)

# Test weakref.proxy() to a function

def f(x):
    return x**2

p = weakref.proxy(f)
print(p)
print(p(2))

print(p is f)

# Test weakref.ref to a class

class C:
    def __init__(self, x):
        self.x = x
    def f(self):
        return self.x**2

i = C(2)
r = weakref.ref(i)
print(r)
print(r().x)
print(r().f())

print(r() is i)

# Test weakref.proxy to a class

class C:
    def __init__(self, x):
        self.x = x
    def f(self):
        return self.x**2
