from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(dir(a))
print(issubclass(type(a),Iterable))
print(isinstance(a,Iterable))
print(isinstance(a,Iterator))
print(isinstance(a,Generator))
print(isinstance(a,FunctionType))

b = [1]
print(type(b))
print(dir(b))
print(issubclass(type(b),Iterable))
print(isinstance(b,Iterable))
print(isinstance(b,Iterator))
print(isinstance(b,Generator))
print(isinstance(b,FunctionType))
