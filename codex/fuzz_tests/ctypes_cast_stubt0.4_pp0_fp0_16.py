import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
# numpy
import numpy as np
nx = np.int32(42)
ny = np.int32(43)
nz = np.int32(44)

print(nx)
print(ny)
print(nz)

print(nx + 10)
print(ny - 10)
print(nz * 10)

print(nx // 3)
print(ny % 2)
print(nz ** 2)

#%%
# numpy
nx = np.int32([42, 43, 44])
ny = np.int32([45, 46, 47])

print(nx)
print(ny)

print(nx + ny)
print(nx - ny)
print(nx * ny)
print(nx / ny)

print(nx // ny)
print(nx % ny)
print(nx ** ny)

#%%
# numpy
nx = np.int32([42, 43,
