import mmap
# Test mmap.mmap
a = np.arange(10)
a
mm = mmap.mmap(a.data, a.shape[0], "r", access=mmap.ACCESS_READ)
mm[1]
mm[:]
b = np.arange(10)
c = np.arange(10)
b == mm[:]
c == a.data[:]
mm[1] = 12
a
c == a.data[:]
c[1] = 12
c
# Test mmap.mmap with write-access
#b[1] = 13
#b.data[1] = 13
#c[:] = b
#c == a.data[:]
a = mmap.mmap(-1, 100, "g", access=mmap.ACCESS_READ)
c = a[1]
c[1] = 13
c
a = np.arange(10)
a.data[1] = 13
a
a.shape
a.flags
a
