import ctypes
ctypes.cast(0, ctypes.py_object).value

# 创建一个空的类
class EmptyClass:
    pass

# 创建一个有属性的类
class Person:
    name = 'liang'
    age = 18

# 创建一个有方法的类
class Person:
    def say_hi(self):
        print('Hello, how are you?')

# 创建一个有构造函数的类
class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello, my name is', self.name)

# 创建一个有继承的类
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
       
