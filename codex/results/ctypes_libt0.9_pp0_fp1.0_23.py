import ctypes
ctypes.c_uint()
ctypes.c_uint64()

a = np.random.rand(10000000)
print float(a[0])
a = np.array(a, dtype=np.uint64) #uint64 is a machine word
print float(a[0])
print a[0:5]
print a.dtype
a.nbytes
a[0]
a.shape
a.shape = (5,5)
a[0,0]
a.shape = (20,500,-1)
a[0,0,0]
a.shape=(1000000,10)
#a.tofile('test.dat')

a.shape = (100000,100)

# a.tofile('test.bin')

# a2 = np.fromfile('test.bin', dtype=np.uint64)
a2 = np.fromfile('test.bin', dtype=np.uint64).reshape(10000,100)
a2[0,0]

a3 = a.copy()
a3 == a2
a3[
