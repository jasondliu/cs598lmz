import ctypes
ctypes.cast(0, ctypes.py_object).value

# 对于ctypes，你还可以使用from_param()方法来确保参数被正确的传递。
# 例如，下面是一个使用ctypes的简单的回调函数：
def callback(x):
    print(x)

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int)
c_callback = CALLBACK(callback)

# 如果你传递一个普通的Python回调函数给这个C函数，会发生什么？
# 实际上，你会得到一个ctypes.CFUNCTYPE实例
