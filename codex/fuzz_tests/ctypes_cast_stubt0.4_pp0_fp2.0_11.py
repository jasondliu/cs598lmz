import ctypes
ctypes.cast(ctypes.pointer(a), ctypes.POINTER(ctypes.c_int32))

# <codecell>

a = np.array([1,2,3,4,5])
a.ctypes.data

# <codecell>

a.ctypes.data_as(ctypes.POINTER(ctypes.c_int32))

# <codecell>

a.ctypes.data_as(ctypes.POINTER(ctypes.c_int32)).contents

# <codecell>

a.ctypes.data_as(ctypes.POINTER(ctypes.c_int32))[0]

# <codecell>

a.ctypes.data_as(ctypes.POINTER(ctypes.c_int32))[0] = 10

# <codecell>

a

# <codecell>

a.ctypes.data_as(ctypes.POINTER(ctypes.c_int32))[1] = 20

# <codecell>

a

# <codecell>
