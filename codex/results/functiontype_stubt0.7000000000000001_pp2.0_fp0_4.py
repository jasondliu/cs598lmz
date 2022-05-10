from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type([]))
print(type(FunctionType))

# 判断对象是否可调用
print(callable([]))
print(callable(FunctionType))
print(callable(max))
print(callable([].append))
print(callable(lambda x: x))

# 类和实例
# 类是对象
class Person:
    pass

p = Person()
print(type(Person))
print(type(p))

# 类属性和实例属性
class Person2:
    name = "Person"

p = Person2()
p.name = "Liu"
print(p.name)
print(Person2.name)
del p.name
print(p.name)

# 构造器
# __init__
class Person3:
    def __init__(self):
        self.
