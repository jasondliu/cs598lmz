from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 判断对象是否为可调用对象
print(callable(isinstance))
print(callable(lambda x: x*2))
print(callable(a))

# 判断对象是否为枚举对象
from enum import Enum

Animal = Enum('Animal', ('Tiger', 'Elephant', 'Cat'))
print(isinstance(Animal.Tiger, Enum))

# 如何判断一个对象是另一个对象的子类？
class A(object):
    pass

class B(A):
    pass

print(isinstance(A(), A))
print(type(A()) == A)

print(isinstance(B(), A))
print(type(B())
