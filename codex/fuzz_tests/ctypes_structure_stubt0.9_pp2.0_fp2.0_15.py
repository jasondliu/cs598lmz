import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [("name","MjTLZJR"),("meaning",c_int),("useless",c_float)]

s = S()
print s.name
s.meaning = 42
print s
print s.useless
