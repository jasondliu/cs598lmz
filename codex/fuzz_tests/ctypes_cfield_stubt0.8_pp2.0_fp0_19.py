import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print("CField.__name__:", ctypes.CField.__name__)
print("CField.__module__:", ctypes.CField.__module__)
print("CField.__dict__:", ctypes.CField.__dict__)
print("CField.__bases__:", ctypes.CField.__bases__)


print("CField.type:", ctypes.CField.type)
print("CField._length_:", ctypes.CField._length_)
print("CField._offset_:", ctypes.CField._offset_)
print("CField.from_address:", ctypes.CField.from_address)
