import types
types.FunctionType
# <type 'function'>

# 判断一个对象是否是函数
def fn():
    pass

print(type(fn) == types.FunctionType)
# True

print(isinstance(fn, types.FunctionType))
# True

# 判断一个对象是否是可调用的
print(callable(fn))
# True

# 使用__call__
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()
# My name is Michael.

# 当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本
