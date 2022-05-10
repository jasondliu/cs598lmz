import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'
fun()

# 在python中调用C函数
# 创建一个c函数
with open('test.c', 'r') as f:
    code = f.read()
with open('test.c', 'w') as f:
    f.write('#include <stdio.h>\n' + code)
# 编译
os.system('gcc -shared -o test.so -fPIC test.c')
# 载入
ctypes.CDLL('./test.so')

# 导入C模块
import sys
sys.path.append('.')
import test
test.fun()

# 创建一个c模块
with open('test.c', 'r') as f:
    code = f.read()
with open('test.c', 'w') as f:
    f.write('''
#include <Python.h>


