import ctypes
# Test ctypes.CFUNCTYPE

# structure.pack is only supported in 3.2
# try:
#     import struct
#     pack = struct.pack
# except:

def pack(fmt, *args):
    return bytes(fmt % args, 'utf-8')

def unpack(fmt, *args):
    return pack(fmt, *args)


class MyStructure(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

def callbackfunc(a, b, pmystruct):
    pmystruct.contents.a *= a
    pmystruct.contents.b += b
    return 0

my_struct = MyStructure(2, 3)

MyFuncType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int,
                              ctypes.POINTER(MyStructure))

myfunc = MyFuncType(callbackfunc)
myfunc(3, 5, my_
