import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
x = np.ones(10)
I = np.random.randint(0,len(x),20)
x[I] *= -1
sign = 2*(x>0)-1

#%%
# from stackoverflow
# https://stackoverflow.com/questions/5671021/how-to-get-the-index-of-the-true-value-in-a-boolean-array-python
y = np.array([0, -1, 1, 0, 1, -1, 1, -1])
# Get the indices of the sign changes
idx = np.where(np.diff(np.sign(y)))[0]
# Get the values at the sign changes
vals = y[idx]
print(vals)

#%%
# from stackoverflow
# https://stackoverflow.com/questions/43305854/find-all-local-maxima-in-a-1d-numpy-array
# Find all local maxima in a 1
