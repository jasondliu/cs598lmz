from types import FunctionType
a = (x for x in [1])
print(type(a))

def a():
    print("hello")

b = a()
# print(type(b))
print(type(a))

# print(type(lambda b: True) == FunctionType)
# print(type(lambda b: True))
# print(type(FunctionType))

print(isinstance((x for x in [1]), GeneratorType))
print(isinstance((x for x in [1]), IteratorType))
