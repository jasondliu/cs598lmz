import types
types.FunctionType

# 判断是否是函数
def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 使用isinstance()
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 使用dir()
print(dir('ABC'))

# len()
print(len('ABC'))
print('ABC'.__len__())

# 实例属性和类属性
class Student(object):
    name = 'Student'

s = Student()
print(s.name)
print(Student.name)
s.name = 'Michael'
print(s.name)
print(Student.name)
