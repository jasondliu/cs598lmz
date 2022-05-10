from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(type(FunctionType))
print(type(a))


def test():
    print("hello world")


print(type(test))
