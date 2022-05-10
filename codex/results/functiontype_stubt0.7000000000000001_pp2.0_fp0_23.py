from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(abs), type(str), type(int), type(dict), type(FunctionType))

# 类型判断
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 类型转换
print(float('12.345'))
print(int(12.34))


# 自定义类型转换函数
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


print(Student('Michael'))

# 判断对象变量是否可以被调用
print(callable(Student))
print(callable(max))

