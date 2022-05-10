from types import FunctionType
a = (x for x in [1])
print(type(a))
# <class 'generator'>

def fun(x):
    return x

print(type(fun))
# <class 'function'>

print(type(lambda x: x))
# <class 'function'>

print(isinstance(fun, FunctionType))
# True

print(isinstance(lambda x: x, FunctionType))
# True

print(type(a) == type(fun))
# False

print(isinstance(a, FunctionType))
# False

print(isinstance(a, type(fun)))
# False

print(isinstance(a, GeneratorType))
# True

print(isinstance(a, type(a)))
# True

print(isinstance(a, list))
# False

print(isinstance(a, (list, GeneratorType)))
# True

print(isinstance(fun, GeneratorType))
# False

print(isinstance(fun, (FunctionType, GeneratorType)))
# True
