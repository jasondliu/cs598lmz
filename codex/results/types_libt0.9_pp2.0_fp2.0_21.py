import types
types.SimpleNamespace

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__


#print(Student('Michael'))


# 类属性和实例属性
class Studen(object):   # 首先将用户名赋值给类变量
    name = 'Student'
s = Studen() # 此时类变量赋值Student
print(s.name)
print(Studen.name)
s.name = 'Michael'  # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高
