from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

# 判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))


# 实例属性和类属性
class Student(object):
    name = 'Student'


s = Student()

print(s.name)
print(Student.name)
s.name = 'Michael'
print(s.name)
print(Student.name)
del s.name
print(s.name)
print(Student.name)

# 练习
# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，
