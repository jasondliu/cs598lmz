import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
x = [1, 2, 3]
y = x
y.append(4)
print(x)

#%%
x = [1, 2, 3]
y = x
y = y + [4]
print(x)

#%%
x = [1, 2, 3]
y = x
y += [4]
print(x)

#%%
x = [1, 2, 3]
y = x
x = x + [4]
print(y)

#%%
x = [1, 2, 3]
y = x
x += [4]
print(y)

#%%
x = [1, 2, 3]
y = x
x = x + [4]
print(y)

#%%
x = [1, 2, 3]
y = x
x += [4]
print(y)

#%%
x = [1, 2, 3]
y = x
x = x + [4]
print(y)


