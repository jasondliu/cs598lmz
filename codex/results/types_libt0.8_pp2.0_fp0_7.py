import types
types.MethodType(instancemethod(cmp,None,list),list)

# 人类
class Person(object):
    # 属性
    age = 0
    # 构造函数
    def __init__(self,age=0):
        self.age = age
    # 实例方法
    def __cmp__(self, other):
        return self.age-other.age
    # 静态方法
    @staticmethod
    def sort(personlist):
        personlist.sort()
    # 类方法
    @classmethod
    def test(cls):
        print 'test'

# 学生类
class Student(Person):
    pass

p1 = Person(80)
p2 = Person(20)
p3 = Person(20)
p4 = Student(20)

# Person.sort([p1,p2,p3])
# print p1.age,p2.age,p3.age

# print c
