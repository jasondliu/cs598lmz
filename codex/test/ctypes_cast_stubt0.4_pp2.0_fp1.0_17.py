import ctypes
ctypes.cast(id(0), ctypes.py_object).value

# 或者使用内置函数
# sys.getrefcount(0)

# 用户自定义的类型
class A:
    pass

a = A()
# sys.getrefcount(a)

# 可变对象
b = [1, 2, 3]
# sys.getrefcount(b)

# 对象的引用计数是动态的，如果创建了一个对象，引用计数为1，
# 如果创建了一个别名，引用计数加1，如果销毁了一个别名，引用计
