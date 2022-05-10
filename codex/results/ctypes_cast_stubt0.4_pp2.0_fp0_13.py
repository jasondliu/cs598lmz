import ctypes
ctypes.cast(id(my_int), ctypes.py_object).value

#%%
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
a is b

a = [1, 2, 3, 4, 5]
b = a
a is b

#%%
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
a == b

a = [1, 2, 3, 4, 5]
b = a
a == b

#%%
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
a is b

a = [1, 2, 3, 4, 5]
b = a
a is b

#%%
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
a == b

a = [1, 2, 3, 4, 5]
b = a
a == b

#%%

