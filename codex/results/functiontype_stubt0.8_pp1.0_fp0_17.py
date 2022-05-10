from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = a.__next__

result = [type(x) for x in [a, b, c]]
print (result)

print (isinstance(a, FunctionType))

# print (a)
# print (b)
# print (c)
