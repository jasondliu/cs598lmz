import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# Here we define the function that we want to make available.
def f(x):
    return x**2

# Now we make the function callable from C.
f_c = FUNTYPE(f)

# Now we can call the function from C.
print f_c(2)

# We can also call it from Python.
print f_c(2)

# And we can even make it a method of a C class.
class C(object):
    def __init__(self):
        self.f = f_c

c = C()
print c.f(2)

# We can also make it a global variable in C.
c.dll.f = f_c
print c.dll.f(2)
</code>

