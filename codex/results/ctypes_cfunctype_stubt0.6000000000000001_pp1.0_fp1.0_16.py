import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello world'

print(fun())
print(type(fun))
print(fun.__name__)
print(fun.__doc__)

####################################################
# 定义一个函数类型
# 函数类型，实际上是一个结构体类型
class FunType(ctypes.Structure):
    _fields_ = [('fun', FUNTYPE)]

f = FunType(fun)
print(f.fun())

####################################################
# 定义一个类型
class Type(ctypes.Structure):
    _fields_ = [('i', ctypes.c_int),
                ('f', ctypes.c_float),
                ('s', ctypes.c_char_p),
                ('fun', FUNTYPE)]

# 创建一个实例
t = Type(1, 2.3, b'some
