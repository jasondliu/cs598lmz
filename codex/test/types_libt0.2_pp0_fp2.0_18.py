import types
types.MethodType(f, None, Student)

# 实例属性和类属性
class Student(object):
    name = 'Student'

s = Student() # 创建实例s
