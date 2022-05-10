import types
types.MethodType(f, None, class_name)

class_name.f()

# 实例属性和类属性
class Student(object):
    name = 'Student'

s = Student()
print(s.name)
