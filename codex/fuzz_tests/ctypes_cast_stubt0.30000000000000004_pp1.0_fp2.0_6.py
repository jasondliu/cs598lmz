import ctypes
ctypes.cast(id(x), ctypes.py_object).value

# Output:
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])

#%%
# NumPy array to Python list structure
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x.tolist()

# Output:
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#%%
# Python list to NumPy array
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np.asarray(x)

# Output:
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])

#%%
# NumPy array to Python list of lists
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x.tol
