import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 可以看到，这个值和上面的 id(obj) 是一样的。
# 这里的 ctypes 是 Python 的一个外部库，它能够让 Python 调用其他语言的代码。
# 其中 py_object 是 ctypes 库里面的一个类型，它能够表示一个 Python 对象。
# 它的 value 属性就是这个 Python 对象。
# 所以，这个代码的作用就是把 id(obj) 所表示的整数转换为一个 Python
