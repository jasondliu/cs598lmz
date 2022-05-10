import types
# Test types.FunctionType
def function():
    pass

print(type(function) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.UnicodeType
print(type(u'abc') == types.UnicodeType)
print(type(u'abc').__name__ == 'unicode')

# Test types.NoneType
print(type(None) == types.NoneType)

# Test types.SliceType
print(type(slice(1, 10, 2)) == types.SliceType)

# Test types.EllipsisType
print(type(Ellipsis) == types.EllipsisType)

# Test types.XRangeType
print(type(xrange(1, 10, 2)) == types.XRangeType)

# Test types.DictProxyType
class MyObject(object):
    def __init__(self):
        self.
