import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 使用ctypes模块把id()函数的返回值转换为一个Python对象。
# 这个技术的一个常见用途就是实现一个弱引用。
# 弱引用的一个用途是为了避免循环引用造成的内存泄漏。
# 循环引用指的是一个对象引用了另一个对象，而后者又引用了前者。
# 一个简单的例子就是一个列表，它包含自
