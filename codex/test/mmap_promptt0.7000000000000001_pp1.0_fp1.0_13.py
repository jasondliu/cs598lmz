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
