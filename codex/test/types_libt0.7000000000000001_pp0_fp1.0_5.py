import types
types.MethodType()

# 实例属性和类属性
class Student(object):
    name = 'Student'

s = Student()
print(s.name)
print(Student.name)
# 给实例绑定属性
s.score = 90
print(s.score)
# 实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
# s.name = 'Michael'
# print(s.name)
# print(Student.name)
# 但是类属性并未消失，用Student.name仍然可以访问
del s.score
print('---------------------------------')

