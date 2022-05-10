from types import FunctionType
a = (x for x in [1])
print(isinstance(a, FunctionType))

a = [x for x in [1]]
print(isinstance(a, FunctionType))

def m():
    return (x for x in [1])
print(isinstance(m(), FunctionType))

def m():
    return [x for x in [1]]
print(isinstance(m(), FunctionType))

def m():
    return 1
print(isinstance(m(), FunctionType))

a = 1
print(isinstance(a, FunctionType))
