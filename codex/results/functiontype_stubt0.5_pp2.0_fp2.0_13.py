from types import FunctionType
a = (x for x in [1])
print(type(a))

b = FunctionType(lambda x: x, globals())
print(b)

c = type('', (), {})
print(c)

# 对象的状态：对象的属性
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('lili', 18)
print(p.__dict__)

# 对象的行为：对象的方法
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print('%s is eating' % self.name)
    def sleep(self):
        print('%s is sleeping' % self.name)

p = Person('lili', 18)
p.eat()
p.sleep()

# 对象的类
