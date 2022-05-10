import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello\n"
strtype = type("")
if isinstance("", strtype):
    print("instance")
print("fun is", repr(fun))
print("fun() is", repr(fun()))
print("function", repr(function))
print("function() is", repr(function()))

from _ctypes_test import func, func_si
print("func(1)=", func(1))
print("func(1, 2)=", func(1, 2))
print("func(1, 2, 3)=", func(1, 2, 3))
print("func(1, 2, 3, 4)=", func(1, 2, 3, 4))
func_si(b"This is a test", ctypes.sizeof(b"This is a test"))
try:
    func_si(b"This is a test", ctypes.sizeof(b"This is a test") - 1)
except ValueError:
    print("passed exception")

try:
    func_si(b"This is a test", ctypes.sizeof(b"This is
