from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type((x for x in [1])))
print(type(FunctionType))
print(type(abs))
print(type(lambda x:x))
print(type((x for x in [1])))
print(type([]))
print(type({}))
print(type(set()))
