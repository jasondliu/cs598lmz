from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 可以通过类的__call__方法让类的实例变成可调用对象
class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)
s = Student('Michael')
s()

# 判断一个对象是否可调用
callable(Student('Michael'))
callable(max)
callable([1, 2, 3])
callable(None)
callable('str')

# 使用枚举类
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name,
