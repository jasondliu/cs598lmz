from types import FunctionType
a = (x for x in [1])
b = [y for y in [1]]
c = {z: z for z in [1]}
d = {z for z in [1]}

print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))
print(isinstance(d, GeneratorType))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(c, FunctionType))
print(isinstance(d, FunctionType))

print(isinstance(a, collections.Generator))
print(isinstance(b, collections.Generator))
print(isinstance(c, collections.Generator))
print(isinstance(d, collections.Generator))


# 泛型类
from typing_extensions import Protocol

class A(Protocol):
    x: int

class B(Protocol):
    x: bool

# def add_A_to_B(a: A, b: B) -> B:
#     return type(b)(
