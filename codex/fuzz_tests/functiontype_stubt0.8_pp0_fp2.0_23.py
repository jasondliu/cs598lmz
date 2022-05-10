from types import FunctionType
a = (x for x in [1])
print(a)

i = iter(a)
print(i)

for j in i:
    print(j)
