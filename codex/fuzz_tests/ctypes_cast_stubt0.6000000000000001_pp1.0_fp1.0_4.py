import ctypes
ctypes.cast(0, ctypes.py_object).value

#%%
a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
a
a[0,:]
a[:,0]
a[1,1:4]
a[:,-1]
a[0,0] = 100
a[1,1:4] = 200
a[:,-1] = 300
a
a[0,0]
a[1,1:4]
a[:,-1]

#%%
b = np.arange(100).reshape(10,10)
b
b[:,0]
b[0,:]
b[1:3,1:3]
b[1:3,1:3] = 0
b

#%%
c = np.arange(1,101).reshape(10,10)
c
c[0,:] = 1
c[:,0] = 1
c[1:9,1:9] = 0
c

#%%
d = np.ar
