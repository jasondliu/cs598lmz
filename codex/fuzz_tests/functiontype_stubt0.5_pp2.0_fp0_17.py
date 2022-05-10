from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, (GeneratorType, FunctionType)))

# 子类继承父类，父类的所有东西都会传给子类，包括父类的方法和属性，子类可以自由的使用
# 子类可以继承父类的方法，也可以重写父类的方法
# 子类可以继承父类的属性，也可以重写父类的属性
class A(object):
   
