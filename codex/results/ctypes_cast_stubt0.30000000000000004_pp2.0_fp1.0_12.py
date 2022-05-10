import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = np.array([7, 8, 9])

np.concatenate([x, y, z])

#%%
x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])

# vertically stack the arrays
np.vstack([x, grid])

#%%
# horizontally stack the arrays
y = np.array([[99],
              [99]])
np.hstack([grid, y])

#%%
#%%
x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)

#%%
grid = np.arange(16).reshape((4, 4))
grid

#%%
upper, lower
