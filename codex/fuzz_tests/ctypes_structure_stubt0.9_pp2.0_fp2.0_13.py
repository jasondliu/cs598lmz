import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32
    _fields_ = [
        ("x", ctypes.c_uint32),
    ]
    S = ctypes.Structure
    _fields_ = [
        ("x", ctypes.c_uint32),
    ]

print(S)  # <class '__main__.S'>
print(S())  # <__main__.S object at 0x7fd1acf9a9e8>


class T(ctypes.Structure, type(ctypes.Structure)):
    _fields_ = [
        ("x", ctypes.c_uint32),
    ]

print(T) # <class '__main__.T'>

print(type(ctypes.Structure)) # <class 'type'>
print(type(type(ctypes.Structure))) # <class 'type'>
print(type(type(type(ctypes.Structure)))) 
print(type(type(type(type(ctypes.Structure))))) # <class 'type'>
print(type(type(type(type(type
