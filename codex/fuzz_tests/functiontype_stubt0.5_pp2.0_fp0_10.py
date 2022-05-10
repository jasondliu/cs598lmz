from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x:x))
print(type(FunctionType))
print(type(FunctionType.__call__))
print(type(FunctionType.__call__.__call__))

print(type(type))
print(type(type.__call__))
print(type(type.__call__.__call__))
print(type(type.__call__.__call__.__call__))
print(type(type.__call__.__call__.__call__.__call__))
print(type(type.__call__.__call__.__call__.__call__.__call__))
print(type(type.__call__.__call__.__call__.__call__.__call__.__call__))
print(type(type.__call__.__call__.__call__.__call__.__call__.__call__.__call__))
print(type(type.__call__.__call__.__call__.__call__.__call__.__call__.__call
