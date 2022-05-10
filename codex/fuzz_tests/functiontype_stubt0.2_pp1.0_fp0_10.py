from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(FunctionType))
print(type(FunctionType(lambda x: x, {})))
print(type(FunctionType(lambda x: x, {}).__call__))
print(type(FunctionType(lambda x: x, {}).__call__(1)))
print(type(FunctionType(lambda x: x, {}).__call__(1).__call__))
print(type(FunctionType(lambda x: x, {}).__call__(1).__call__(2)))
print(type(FunctionType(lambda x: x, {}).__call__(1).__call__(2).__call__))
print(type(FunctionType(lambda x: x, {}).__call__(1).__call__(2).__call__(3)))
print(type(FunctionType(lambda x: x, {}).__call__(1).__call__(2).__call__(3).__call__))
print(type(FunctionType(lambda x: x, {}).__call__(1).__
