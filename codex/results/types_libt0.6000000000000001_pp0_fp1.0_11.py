import types
types.ClassType

# 类别
class Person:
    pass

p = Person()
p.name = "Bart"
p.gender = "Male"

# 方法
class Person:
    def sayHi(self):
        print "Hello,how are you"

p = Person()
p.sayHi()

# 构造函数
class Person:
    def __init__(self,name):
        self.name = name
    def sayHi(self):
        print "Hello,my name is",self.name

p = Person("Swaroop")
p.sayHi()

# 继承
class SchoolMember:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print "Initialized SchoolMember:%s"%self.name
    def tell(self):
        print "Name:%s Age:%s"%(self.name,self.age)

class Teacher(SchoolMember):
    def __init__(self,
