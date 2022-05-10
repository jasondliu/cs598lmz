import types
types.MethodType

#静态方法和类方法
class Student(object):
    @staticmethod
    def add(x,y):
        return x+y
    @classmethod
    def add2(cls,x,y):
        return cls(x+y)
#把Student类的add方法转换为静态方法，直接调用
print(Student.add(1,2))
#把Student类的add2方法转换为类方法，直接调用
print(Student.add2(1,2))

#多继承
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')
