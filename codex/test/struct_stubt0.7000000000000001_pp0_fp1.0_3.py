from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('format','I 2s f')
s.size = s.calcsize(s.__getattribute__('format'))
print(s.size)

# Python中的构造器
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say_hi(self):
        print('Hello,my name is ',self.name)

p = Person('Swaroop',28)
p.say_hi()

# 基于类的类型设计
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember:{})'.format(self.name))

