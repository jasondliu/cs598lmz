import ctypes
ctypes.cast(id(a), ctypes.py_object).value

#%%

a = np.zeros((2,2))
a[0,0] = 1
a[0,1] = 2
a[1,0] = 3
a[1,1] = 4

b = np.zeros((2,2))
b[0,0] = 5
b[0,1] = 6
b[1,0] = 7
b[1,1] = 8

c = np.zeros((2,2))
c[0,0] = 9
c[0,1] = 10
c[1,0] = 11
c[1,1] = 12

#%%

a = np.zeros((2,2))
a[0,0] = 1
a[0,1] = 2
a[1,0] = 3
a[1,1] = 4

b = np.zeros((2,2))
b[0,0] = 5
b[0,1] = 6
b[1,0] =
