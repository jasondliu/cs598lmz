import weakref
# Test weakref.ref(function)

def f():
    return 42

r = weakref.ref(f)
print(r)
print(r())

# Test weakref.ref(class)

class C:
    def __init__(self):
        self.x = 42

c = C()
r = weakref.ref(c)
print(r)
print(r().x)

# Test weakref.ref(instancemethod)

class D:
    def f(self):
        return 42

d = D()
r = weakref.ref(d.f)
print(r)
print(r()())

# Test weakref.ref(builtin_function)

r = weakref.ref(len)
print(r)
print(r()("abc"))

# Test weakref.ref(builtin_method)

r = weakref.ref("abc".__len__)
print(r)
print(r()())

# Test weakref.ref(method)

class E:
    def f(self):
        return 42
