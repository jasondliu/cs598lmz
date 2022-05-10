from types import FunctionType
a = (x for x in [1])
print(isinstance(a, FunctionType))

a= [1,2,3]
print(a[0])
print(a[1])
print(a[2])
print(a[3])

a = 'a'
print('a.isalnum() = ', a.isalnum())
a = '1'
print('a.isalnum() = ', a.isalnum())
