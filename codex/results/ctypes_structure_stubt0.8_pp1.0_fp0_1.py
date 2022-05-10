import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double
    w = ctypes.c_double

m = np.random.rand(100,100,100)

print(m.flags.f_contiguous)

arr = np.ctypeslib.as_ctypes(m)
print(type(arr))
print(arr._type_)
print(arr._length_)

data = S.from_address(ctypes.addressof(arr))
print(data.x,data.y,data.z,data.w)

print(data.x._type_)

print(arr._objects)
print(sys.getrefcount(data))

print(sys.getrefcount(arr))

a = np.array([[1, 2, 3], [4, 5, 6]],)
print(a.dtype)
print(a.flags)
# sys.exit()

start_time = time.time()
for i in range(1000):
    a = np.random
