import ctypes
FUNTYPE = ctypes.CFUNCTYPE(c_bool)
def t(x):
    print x
print t(1) # True

f = lambda x: x > 4

pf = FUNTYPE(f)
print pf(3) # False

x = 3
print ctypes.cast(id(x), ctypes.POINTER(ctypes.c_int))

print f(3)
print f(5)
print f(34)

```

```python
import ctypes

def f(x):
    return x > 5

FUNTYPE = ctypes.CFUNCTYPE(c_bool)
pf = FUNTYPE(f)
pf(4) # False

# or

pf = FUNTYPE(lambda x: x > 4)
pf(4) # False

# or

pf = (c_bool).from_address(id(f))
pf(4) # False

# or

pf = (c_bool).from_address(id(lambda x: x > 4))
pf(4) # False

#
