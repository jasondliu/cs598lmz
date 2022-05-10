from types import FunctionType
a = (x for x in [1])
print(type(a))

def foo():
    pass

print(type(foo))
print(type(FunctionType))
print(type(type))

# 创建类
class Dog(object):
    pass

print(Dog)
d = Dog()
print(d)

# 定义一个类
class Dog(object):
    def __init__(self, name):
        self.name = name

d = Dog('yellow')
print(d)
print(d.name)

# 创建一个字典
d = dict(name='yellow', age=2)
print(d)

# 创建一个实例
class Dog(object):
    def __init__(self, name):
        self.name = name

d = Dog('yellow')
print(d)
print(d.name)

# 打印实例
class Dog(object):
    def __init__(self
