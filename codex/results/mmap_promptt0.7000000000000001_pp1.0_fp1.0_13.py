import mmap
# Test mmap.mmap(0, 1, "ABC")

# Must be able to pass a writable buffer as the initializer
class MyMemoryView(memoryview):
    def __init__(self, init):
        memoryview.__init__(self, init)
    def __del__(self):
        memoryview.__del__(self)

a = bytearray("ABC")
b = MyMemoryView(a)
print len(b)
print b.tobytes()

# Basic properties
print memoryview(a).itemsize
print memoryview(a).nbytes
print memoryview(a).ndim
print memoryview(a).shape
print memoryview(a).strides
print memoryview(a).suboffsets

# Make sure we can hash it
print hash(memoryview(a))

# Make sure we can slice it
print memoryview(a)[0]
print memoryview(a)[1:]
print memoryview(a)[-2:]

# Make sure we can slice it in various ways
print memoryview(a)[1:1]
print memoryview(a)[
