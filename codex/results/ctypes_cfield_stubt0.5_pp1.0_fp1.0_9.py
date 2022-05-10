import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFoo(ctypes.CField):
    def __get__(self, obj, objtype):
        print "get"
        return self.__get_field__(obj)

    def __set__(self, obj, value):
        print "set"
        self.__set_field__(obj, value)

class C(ctypes.Structure):
    _fields_ = [('x', CFoo)]

print C.x
print C.x.__get__(S(1), S)
C.x.__set__(S(1), 2)
print C.x.__get__(S(1), S)
</code>

