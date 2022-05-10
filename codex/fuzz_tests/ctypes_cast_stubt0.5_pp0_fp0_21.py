import ctypes
ctypes.cast('B', ctypes.pointer(ctypes.c_int(127)))

# <codecell>

a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)
np.concatenate((a,b), axis=0)

# <codecell>

np.concatenate((a,b), axis=1)

# <codecell>

a = np.arange(24).reshape(2,3,4)
b = np.arange(24,48).reshape(2,3,4)
np.concatenate((a,b), axis=0)

# <codecell>

np.concatenate((a,b), axis=1)

# <codecell>

np.concatenate((a,b), axis=2)

# <codecell>

np.concatenate((a,b), axis=-1)

# <codecell>

np.concatenate((a,b
