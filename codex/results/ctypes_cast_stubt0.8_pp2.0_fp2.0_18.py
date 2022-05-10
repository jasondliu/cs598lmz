import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 6.15 通过字符串调用对象的属性
# 问题: 你有一个对象实例，它有很多的属性，但是你想通过名称来访问这些属性。
# 解决方案: 使用 getattr() 函数来访问一个对象的属性。下面是一个使用这个函数的交互式例子。
class person:
    def __init__(self):
        self.name = 'Bob'
obj = person()
res = getattr(obj, 'name')
print(res)

# 6.16
