import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong()
    def __repr__(self):
        return "<%s.%s object at %#x>" % (
            self.__class__.__module__,
            self.__class__.__name__,
            id(self))

s = S()
s.x = 42
print(s)
print(s.x)
print(type(s.x))
s.x = "abc"
print(s.x)
print(type(s.x))
s.x = 0x1234567890abcdef
print(s.x)
print(type(s.x))
#s.x = 0x1234567890abcdef1234567890abcdef
#print(s.x)
#print(type(s.x))

class S64(ctypes.Structure):
    _fields_ = [("x", ctypes.c_longlong)]
    def __repr__(self):
        return "<%s.%s object at %#x>" % (
            self.__class__.__
