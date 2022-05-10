from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(abs))
print(type(lambda x: x))
print(type(x for x in range(10)))

print("========================")

# 判断一个变量是否是函数
print(isinstance(abs, FunctionType))
print(isinstance(lambda x: x, FunctionType))
print(isinstance((x for x in range(10)), FunctionType))
print(isinstance(a, FunctionType))

print("========================")

# 使用__str__
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__
print(Student("Michale"))

print("========================")

# 使用__iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__
