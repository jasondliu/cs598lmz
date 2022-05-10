import mmap
# Test mmap.mmap - open file, map entire file to memory, read from mmap
f = open("testfile.txt", "r+")
# memory-map the file, size 0 means whole file
mf = mmap.mmap(f.fileno(), 0)
print("Reading testfile.txt via mmap:")
print("mf[0:3]    = %r" % mf[0:3])
print("mf[:3]     = %r" % mf[:3])
print("mf[1:3]    = %r" % mf[1:3])
print("mf[1:1]    = %r" % mf[1:1])
print("mf[10:]    = %r" % mf[10:])
print("mf[:-1]    = %r" % mf[:-1])
print("mf[-3:]    = %r" % mf[-3:])
print("mf[-4:-2]  = %r" % mf[-4:-2])
