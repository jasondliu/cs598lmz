import ctypes
ctypes.cast(id(x), ctypes.py_object).value

# %%
import sys
sys.getrefcount(x)

# %%
y = x
sys.getrefcount(x)

# %%
del x
sys.getrefcount(y)

# %%
import ctypes
ctypes.cast(id(y), ctypes.py_object).value

# %%
import weakref
a_set = {0, 1}
wref = weakref.ref(a_set)
wref

# %%
wref()

# %%
a_set = {2, 3, 4}
wref()

# %%
wref() is None

# %%
wref() is None

# %%
import sys
sys.getrefcount(a_set)

# %%
del a_set
sys.getrefcount(a_set)

# %%
wref() is None

# %%
import weakref
class Cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(
