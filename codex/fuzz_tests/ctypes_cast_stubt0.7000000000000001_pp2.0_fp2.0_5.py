import ctypes
ctypes.cast(ctypes.addressof(x),ctypes.POINTER(ctypes.c_double)).contents

# check the address of x and its content
print(ctypes.addressof(x))
print(ctypes.cast(ctypes.addressof(x),ctypes.POINTER(ctypes.c_double)).contents)

# change the content in memory with ctypes
ctypes.cast(ctypes.addressof(x),ctypes.POINTER(ctypes.c_double)).contents.value = 3
print(x)
x = 0

# create a class in ctypes
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

# create an instance of Point
p = Point()

# check the address of p and its content
print(ctypes.addressof(p))
print(ctypes.cast(ctypes.addressof(p),ctypes.POINTER(ctypes.c_double)).contents)
print(p
