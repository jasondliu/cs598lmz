from types import FunctionType
a = (x for x in [1])

print map(FunctionType, dir(a))

for i in a:
    print i
