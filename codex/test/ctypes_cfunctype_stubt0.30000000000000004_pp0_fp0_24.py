import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())

# 这个例子中，我们定义了一个函数类型，返回值是 py_object，这是一个特殊的类型，可以接受任何 Python 对象。
# 然后，我们定义了一个函数，这个函数返回一个字符串。
# 最后，我们调用这个函数，并打印出返回的字符串。

# 如果你想要调用一个 C 函数，你可以使用 ctypes
