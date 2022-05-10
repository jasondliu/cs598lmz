from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = map(str, [1,2,3])
d = FunctionType(lambda: None, {})
print type(a), type(b), type(c), type(d)
print type(object)
print '================='
print isinstance([1], Iterable)
print isinstance([1], Iterator)
print isinstance(iter([1]), Iterator)
print isinstance(iter([1]), Iterable)
print '================='
for i in Iterable:
    print i
print '================='
for i in Iterator:
    print i
