from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(print))
print(type(FunctionType))

# 判断对象是否是函数
print(callable(print))
print(callable(a))
print(callable(FunctionType))

# 函数对象有一个__call__()方法，我们可以把对象当函数调用
class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()

# 使用callable()函数，就可以判断一个对象是否是“可调用”对象。
print(callable(Student('Michael')))
print(callable(
