import weakref
# Test weakref.ref(int)
def f():
    return 42

w = weakref.ref(f())
v = w()
print(v)

w = weakref.ref(f)
v = w()
print(v())

# Test weakref.ref(function)
def f():
    pass

w = weakref.ref(f)
v = w()
print(v)

# Test weakref.ref(instance method)
class C:
    def f(self):
        pass

c = C()
w = weakref.ref(c.f)
v = w()
print(v)

# Test weakref.ref(class method)
class C:
    def f(cls):
        pass
    f = classmethod(f)

w = weakref.ref(C.f)
v = w()
print(v)

# Test weakref.ref(static method)
class C:
    def f():
        pass
    f = staticmethod(f)

w = weakref.ref(C.f)
v = w
