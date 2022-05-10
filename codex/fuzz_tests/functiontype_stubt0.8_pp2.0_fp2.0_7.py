from types import FunctionType
a = (x for x in [1])
b = (x for x in 'hello')
c = (x for x in range(10))
d = (x for x in xrange(10))
print type(a)
print type(b)
print type(c)
print type(d)

print isinstance(a, types.GeneratorType)
print isinstance(b, types.GeneratorType)
print isinstance(c, types.GeneratorType)
print isinstance(d, types.GeneratorType)

print type(a) is types.GeneratorType
print type(b) is types.GeneratorType
print type(c) is types.GeneratorType
print type(d) is types.GeneratorType

print types.GeneratorType is GeneratorType

print types.FunctionType is type(isinstance)
print types.FunctionType is type(zip)
print types.FunctionType is type(map)
print types.FunctionType is type(eval)

print types.FunctionType is type(__import__)
print types.FunctionType is type(Input)

print '---------------------------'
a = (
