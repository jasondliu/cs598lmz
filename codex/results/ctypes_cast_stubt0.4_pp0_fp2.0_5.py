import ctypes
ctypes.cast(0, ctypes.py_object).value

# 一个非常简单的例子，但是这个方法可以用在更多的场合，比如实现一个__getattr__()方法，或者构造一个能够让实例属性透明访问类属性的类等等。

# 下面是一个简单的例子，演示了如何使用ctypes来访问结构体成员：

import ctypes

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int
