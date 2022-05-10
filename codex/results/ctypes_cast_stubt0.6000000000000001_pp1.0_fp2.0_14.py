import ctypes
ctypes.cast(a, ctypes.py_object).value

a = np.arange(10)
b = a
a.shape = 2,5

b.shape

# Python passes mutable objects as references, so function calls make no copy

def f(x):
    print(id(x))

id(a)
f(a)

# the view method creates a new array object that looks at the same data
c = a.view()
c is a

c.base is a # c is a view of the data owned by a

c.flags.owndata

c.shape = 5,2

# Slicing an array returns a view of it
s = a[:, 1:3]
s[:] = 10

a

# Deep Copy
d = a.copy()
d is a

d.base is a # d doesn't share anything with a

d[0,0] = 9999

a
