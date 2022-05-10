import ctypes
# Test ctypes.CField

from ctypes import *

class S(Structure):
    _fields_ = [
        ('value', c_int)
    ]

    def __int__(self):
        return self.value

class S2(Structure):
    _fields_ = [
        ('value', c_int)
    ]

class Test(Structure):
    _fields_ = [
        ('name', c_char_p),
        ('s1', S),
        ('s2', POINTER(S2))
    ]

    def __repr__(self):
        return "<Test instance: name=%s, s1=%d, s2=%d>" % (self.name, int(self.s1), int(self.s2.contents))

t = Test("foo")
print t
t.s1.value = 10
print t
t.s2 = pointer(S2(5))
print t
t.s2.contents.value = 5
print t
