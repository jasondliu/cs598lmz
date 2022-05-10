import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double

class W(ctypes.Structure):
    _fields_ = [("y",ctypes.c_double),("z",ctypes.c_double),("x",ctypes.c_double)]

y = np.zeros(10000,dtype=S)
x = np.zeros(10000,dtype=W)

y = np.frombuffer(y,dtype=S)
x = np.frombuffer(x,dtype=W)

y.x.sum()

y.z.sum()

y.y.sum()

x.z.sum()

x.y.sum()

x.x.sum()

x = np.zeros(10000,dtype=dict(names=["x","y","z"],formats=["f","f","f"],offsets=[16,8,0]))

x.x.sum()

y = np.zeros(10000,dtype=dict(names=
