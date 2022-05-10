import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

# fromStruct()
s = S()
# fromStruct(s) without args doesn't work since we don't have a way to get the structure type from the struct value if it isn't a pointer.
fromStruct(s, S)
fromStruct(s.x)
fromStruct(s.y)

# toStruct()
fromStruct("hello")
fromStruct("hello", ctypes.c_char_p)
fromStruct("hello") # repr should not throw
fromStruct("hello", ctypes.c_char_p).__class__
fromStruct("hello", ctypes.c_char_p).value
fromStruct("hello", ctypes.c_char_p).__int__()
fromStruct("hello", ctypes.c_char_p).__float__()
fromStruct("hello", ctypes.c_char_p).__str__()
fromStruct("hello", ctypes.c_char_
