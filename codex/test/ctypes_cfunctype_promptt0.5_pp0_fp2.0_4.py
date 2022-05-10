import ctypes
# Test ctypes.CFUNCTYPE
def f(x): return x

# CFUNCTYPE(restype, *argtypes)
Cf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# convert callable object to function pointer
cf = Cf(f)
print(cf(1))

# convert function pointer to callable object
cf = Cf(f)
print(cf(1))

# convert function pointer to callable object
cf = Cf(f)
print(cf(1))

# convert function pointer to callable object
cf = Cf(f)
print(cf(1))

# convert function pointer to callable object
cf = Cf(f)
print(cf(1))

# convert function pointer to callable object
cf = Cf(f)
print(cf(1))

# convert function pointer to callable object
cf = Cf(f)
print(cf(1))

# convert function pointer to callable object
cf = Cf(f)
print(cf(1))

# convert function pointer to callable object
cf
