import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
# If you want to get the memory address of a variable, you can use the id function:
a = 5
id(a)

#%%
# The id function returns an integer that is unique for a given object.
# It is guaranteed to be unique and constant for this object during its lifetime.
# The id is not guaranteed to be unique across different objects,
# and it is not guaranteed to be the same from one run to the next.
# This is because the memory address may be reused for other objects.

#%%
import ctypes
ctypes.cast(id(a), ctypes.py_object).value

#%%
# If you want to get the memory address of a variable, you can use the id function:
a = 5
id(a)

#%%
# The id function returns an integer that is unique for a given object.
# It is guaranteed to be unique and constant for this object during its lifetime.
# The id is not guaranteed to be unique across different objects,
# and it is not guaranteed to be the same from one run
