from types import FunctionType
a = (x for x in [1])
print(a)
print(next(a))
print(next(a))

# 函数类型
print(type(abs))
print(type(str))
print(type(FunctionType))
print(type(lambda x: x))

# 实例属性
class Student(object):
    pass

s = Student()
s.name = "Michael"
print(s.name)

# 实例的属性和类的属性名称是相同的，因此，实例属性会屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
class
