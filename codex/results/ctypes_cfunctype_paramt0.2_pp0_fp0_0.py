import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

f = FUNTYPE(func)
print(f(2))

# 使用ctypes.pythonapi.PyCapsule_New()创建一个Capsule对象
# 参数1：Capsule的名称
# 参数2：Capsule的内容
# 参数3：Capsule的销毁函数
# 参数4：Capsule的销毁函数的参数

import ctypes
import sys

def destroy(name, p):
    print('Destroying capsule %s' % name)
    ctypes.pythonapi.PyMem_Free(p)

capsule = ctypes.pythonapi.PyCapsule_New(
    ctypes.py_object(123),
    b'example.capsule
