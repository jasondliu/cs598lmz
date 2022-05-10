import ctypes
ctypes.cast(addr, ctypes.py_object).value

# 2
class MWSText(Text):
    def __getitem__(self, index):
        if index < 0 or index >= self.__len__():
            return "out of index"
        return super(MWSText, self).__getitem__(index)


# 3
from ctypes import c_ubyte, pointer, POINTER
class MWSMemory():
    mws_mem = ctypes.windll.kernel32.GlobalAlloc.argtypes(c_ubyte * 256)
    mws_mem = self.mws_mem()
    pointer(c_ubyte * 256)
    self.mws_mem = pointer(pi)


# 4.1
def sum_of_sq(m):
    for i in range(1, m+1):
        for j in range(1, m+1):
            sum = 0
            sum += i * j
            yield sum
# 4.2
sum(num for num in sum_of_sq(10))
# 4.3

