from types import FunctionType
a = (x for x in [1])
b = (x+1 for x in a)
c = (x+2 for x in b)
for i in c:
    print(i)
