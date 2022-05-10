from types import FunctionType
a = (x for x in [1])
print(a)
print(a.__next__())
# a.__next__()

def test(x):
    print(x)

print(type(test) == FunctionType)
