from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(a == b)

a = FunctionType(lambda x: x, {})
b = FunctionType(lambda x: x, {})
print(a is b)
print(a == b)

a = FunctionType(lambda x: x, {}, 'foo')
b = FunctionType(lambda x: x, {}, 'foo')
print(a is b)
print(a == b)

print(FunctionType(lambda x: x, {}) is FunctionType(lambda x: x, {}))
print(FunctionType(lambda x: x, {}) == FunctionType(lambda x: x, {}))
print(FunctionType(lambda x: x, {}, 'foo') is FunctionType(lambda x: x, {}, 'foo'))
print(FunctionType(lambda x: x, {}, 'foo') == FunctionType(lambda x: x, {}, 'foo'))

print(FunctionType(lambda x: x, {}, 'foo') is FunctionType(lambda x: x, {}, 'bar'
