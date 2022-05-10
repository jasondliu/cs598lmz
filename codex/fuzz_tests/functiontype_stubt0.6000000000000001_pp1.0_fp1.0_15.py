from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a,Iterable))
print(isinstance(a,Iterator))
print(isinstance(a,Iterable))
print(isinstance(a,Iterator))
print(isinstance(a,FunctionType))

print('*'*50)

b = [1,2,3,4]
print(type(b))
print(isinstance(b,Iterable))
print(isinstance(b,Iterator))
print(isinstance(b,Iterable))
print(isinstance(b,Iterator))
print(isinstance(b,FunctionType))

print('*'*50)

c = {'name':'jk','age':18}
print(type(c))
print(isinstance(c,Iterable))
print(isinstance(c,Iterator))
print(isinstance(c,Iterable))
print(isinstance(c,Iterator))
print(isinstance(c,FunctionType))
