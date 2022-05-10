from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)

# 判断一个类型是否是函数
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 判断一个对象是否是函数
print(callable(abs))
print(callable(lambda x: x))
print(callable(a))

# 使用dir()
print(dir('ABC'))
print('ABC'.__len__())
print(len('ABC'))

# 实例属性和类属性
class Student(object):
    name = 'Student'

s = Student()
print(s.name)
print(Student.name)

