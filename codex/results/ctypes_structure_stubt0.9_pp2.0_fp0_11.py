import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    def __init__(self):
        self.x = -1
    def func_0(self):
        self.x = 0
    def func_1(self):
        self.x = 1

buf = ctypes.create_string_buffer("aaaaaaaa", 8)
s = ctypes.cast(ctypes.pointer(buf), ctypes.POINTER(S))
s.contents.func_0()
s.contents.func_1()
s.contents.func_0()
s.contents.func_1()
s.contents.func_0()
s.contents.func_1()
s.contents.func_0()
s.contents.func_1()
s.contents.func_0()
s.contents.func_1()
s.contents.func_0()
s.contents.func_1()
s.contents.func_0()
s.contents.func_1()
s.contents.func_0()
s.contents.func_
