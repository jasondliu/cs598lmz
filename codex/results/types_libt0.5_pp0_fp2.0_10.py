import types
types.MethodType

# 实例属性和类属性
class Student(object):
    # 类属性
    name = 'Student'

# 实例属性
s = Student()
s.score = 90

# 类属性
print(Student.name)
print(s.name)

print(Student.score)
print(s.score)
