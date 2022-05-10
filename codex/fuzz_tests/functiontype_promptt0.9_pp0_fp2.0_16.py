import types
# Test types.FunctionType
def testfunc():
    print("Hello world")
if type(testfunc) == types.FunctionType:
    print("This is a function")

# Test types.LambdaType
teststr = lambda x,y : x + y
if type(teststr) == types.LambdaType:
    print("This is a lambda function")

# Test types.frozenset
print("This is a frozen set: ", frozenset())

# Test types.GeneratorType

# Test types.GeneratorType

# Test types.TracebackType

# Test types.GetSetDescriptorType

# Test types.MemberDescriptorType

# Test types.DictProxyType

# Test types.EllipsisType

# Test types.NotImplementedType

# Test types.TypeType
