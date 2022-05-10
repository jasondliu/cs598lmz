from types import FunctionType
a = (x for x in [1])

print(isinstance(a,FunctionType))
"""
def a():
    yield 1

print(type(a) == FunctionType)
"""
