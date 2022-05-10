import ctypes
ctypes.cast(100, ctypes.py_object).value
import sys
sys.getrefcount(100)
ctypes.cast(100, ctypes.py_object).value = -1
sys.getrefcount(100)
id(100)
id(10000)
# 注：int creates long if int is too large
type(100000000000000000000)
100000000000000000000.0
type(100000000000000000000.0)
a = 3
b = 3
c = 3
a is b
a is c
# 那么从这个简单的例子我们可以看出来，在 python 中，对于小的数字，python 中的整数对象是共享的（所有指向同一个对象），这个整数对象的创建是共享的（
