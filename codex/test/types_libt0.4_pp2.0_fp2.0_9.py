import types
types.FunctionType

# 判断是否是可调用对象
callable(max)
callable([1, 2, 3])
callable(None)
callable('str')

# 使用callable()来替代内置的hasattr()
class Person(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

p = Person('Michael')
p()
callable(p)

# 使用callable()判断一个对象是否是“可调用”对象
# 可调用对象：函数、方法、lambda函数、生成器函数、类、实例
# 不可调用对象
