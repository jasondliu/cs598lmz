import weakref
# Test weakref.ref to a class method

class C(object):
    def f(self):
        return "C.f"

    def g(self):
        return "C.g"

obj = C()

# Get references to the class methods
c_f = C.f.__get__(obj, C)
c_g = C.g.__get__(obj, C)

# Create weak references to the class methods
w_f = weakref.ref(c_f)
w_g = weakref.ref(c_g)

# Delete the object
del obj

# The weak references are still alive
print(w_f())
print(w_g())
