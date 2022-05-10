import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p

class C(object):
    def __init__(self):
        self.__s = S()

c = C()
print(c._C__s)
</code>

