import types
# Test types.FunctionType
def f():pass
print(type(f) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.MethodType
class Person:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        return 'A'

p = Person('Bob', 90)
print(p.get_grade())

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
p.set_age = MethodType(set_age, p) # 给实例绑定一个方法
p.set_age(25) # 调用实例方法
print(
