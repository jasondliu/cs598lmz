from types import FunctionType
a = (x for x in [1])

def f(): pass

print(type(a) is GeneratorType)
print(type(f) is FunctionType)
