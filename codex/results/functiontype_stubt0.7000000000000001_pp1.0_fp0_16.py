from types import FunctionType
a = (x for x in [1])
b = [1]

def test():
    pass

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(test, FunctionType))
