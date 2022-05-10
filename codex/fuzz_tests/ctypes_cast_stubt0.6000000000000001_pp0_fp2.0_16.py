import ctypes
ctypes.cast(0, ctypes.py_object)

# %%
'''
As you can see, this works:
'''

# %%
ctypes.cast(0, ctypes.py_object).value

# %%
'''
So what happens if we use this technique on a class?
'''

# %%
class MyClass:
    pass

# %%
m = MyClass()
ctypes.cast(id(m), ctypes.py_object).value

# %%
'''
So we can get the correct object back, but notice that the `id()` of the object is different 
from the `id()` of the object we got from `ctypes`.
'''

# %%
id(m), id(ctypes.cast(id(m), ctypes.py_object).value)

# %%
'''
This is because the object returned from `ctypes` is a `weakref` object, and not the actual object.
'''

# %%
ctypes.cast(id(m), ctypes.py_object).value

# %%
''
