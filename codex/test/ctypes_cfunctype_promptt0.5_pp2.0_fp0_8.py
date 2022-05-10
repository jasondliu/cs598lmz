import ctypes
# Test ctypes.CFUNCTYPE
@ctypes.CFUNCTYPE(ctypes.c_int)
def my_callback(arg):
    print("my_callback called with", arg)
    return 0

# Test ctypes.POINTER
class MyStructure(ctypes.Structure):
    pass
MyStructure._fields_ = [
    ('a', ctypes.c_int),
    ('b', ctypes.c_int)
]
MyStructure_p = ctypes.POINTER(MyStructure)

# Test ctypes.byref
my_structure = MyStructure()
my_structure.a = 1
my_structure.b = 2

# Test ctypes.addressof
my_structure_p = ctypes.addressof(my_structure)

# Test ctypes.cast
class OtherStructure(ctypes.Structure):
    pass
OtherStructure._fields_ = [
    ('c', ctypes.c_int),
    ('d', ctypes.c_int)
]
OtherStructure_p = ctypes.POINTER
