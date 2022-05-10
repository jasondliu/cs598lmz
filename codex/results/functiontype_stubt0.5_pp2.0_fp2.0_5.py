from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))

def test():
    yield 1

print(isinstance(test(), GeneratorType))

class A:
    pass

print(isinstance(A(), A))
