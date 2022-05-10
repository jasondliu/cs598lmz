import ctypes
ctypes.cast(0, ctypes.py_object).value

# 与之对应的是 ctypes.pythonapi，它是一个 ctypes.PyDLL 对象，它包含了所有的 Python/C API 函数。
# 下面是一个简单的例子，使用 ctypes 调用 Python/C API 函数 Py_GetVersion()：
import sys
from ctypes import pythonapi, c_char_p
version = c_char_p()
pythonapi.Py_GetVersion(ctypes.byref(version))
print(version.value)
print(sys.version)

# 可以看到，ctypes.pythonapi.Py_GetVersion() 函数的返回值是一个 c_char_p 对象，
# 它的 value 属性是一
