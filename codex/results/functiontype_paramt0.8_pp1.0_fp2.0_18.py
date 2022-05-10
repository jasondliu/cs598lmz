from types import FunctionType
list(FunctionType(str,str))

a = [1,2,3]
list(map(str,a))

a = (1,2,3)
list(map(str,a))

# enumerate
a = list(map(str, [1,2,3]))
b = list(enumerate(a))
print(a,b)

a = [1,2,3]
b = list(enumerate(a))
print(a,b)

a = [1,2,3]
b = list(enumerate(a,1))
print(a,b)

a = [1,2,3]
b = list(enumerate(a))
for index, value in b:
    print(index, value)

a = [1,2,3]
for index, value in enumerate(a):
    print(index, value)

# zip
a = [1, 2, 3]
b = [10, 20]
for i, j in zip(a, b):
    print(i, j)

