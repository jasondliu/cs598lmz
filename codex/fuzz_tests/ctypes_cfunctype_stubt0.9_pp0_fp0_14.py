import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return sys.modules[fun.__module__]


# Do it again, using a different name
class mod:
    pass
mod = mod()
mod.fun = FUNTYPE(fun)

del sys.modules[__name__]  # trick: remove the module from the system

# Call the function, get the module back, keep a reference
cur_module = mod.fun()

# When the module is deleted, its globals are also deleted
del mod

# However, we still have the reference
assert cur_module.__dict__ is not None

# Generate a random string
import random
s = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(50))
assert s in cur_module.__dict__  # should be in globals

# When the module is deleted, its globals are also deleted
del cur_module
assert s in globals()  # should still be in globals
got = globals()[s]
assert got.__name__ == s  # globals should return the expected object

