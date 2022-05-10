import ctypes
ctypes.cast(ctypes.pointer(c_int(0)), ctypes.py_object).value = 'spam'

#使用__slots__
class C:
    __slots__ = ['a', 'b']
    def __init__(self):
        self.a = 1
        self.b = 2

# 它是用来限制实例属性名的
# 如果我们想要限制实例的属性，例如，只允许对Student实例添加name和age属性
# 因为age小于18，输出提示信息

class Student(object):
    __slots__ = ('name', 'age')

s = Student() # 创建新的实例
s.name = '
