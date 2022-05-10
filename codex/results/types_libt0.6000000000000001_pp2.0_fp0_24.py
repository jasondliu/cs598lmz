import types
types.MethodType(func, None)

# 实例属性和类属性
class Student(object):
    name = 'Student'

s = Student() # 创建实例s
print(s.name)
print(Student.name)
s.name = 'Michael' # 给实例绑定name属性
print(s.name)
print(Student.name)
del s.name # 删除实例的name属性
print(s.name)
print('------------------------------------------')

# 使用__slots__
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定
