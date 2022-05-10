import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print('hello, world')
    return 1
fun()

# 访问与修改结构体成员
class StructPointer(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
s = StructPointer(1, 2)
print(s.x, s.y)
s.x = 3
s.y = 4
print(s.x, s.y)

# 访问与修改数组成员
class Array(ctypes.Structure):
    _fields_ = [('array', ctypes.c_int * 3)]
a = Array()
a.array[0] = 0
a.array[1] = 1
a.array[2] = 3
print(a.array[0], a.array[1], a.array[2])

# 访问与修改字符串成
