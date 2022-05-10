import types
# Test types.FunctionType and types.MethodType

def test(test,test2):
    print "Test function"

# See if we can test types
if type(test) == types.FunctionType:
    print "Function"
if type(test) == types.MethodType:
    print "Method"

# Now see if we can test subtypes
if isinstance(test, types.FunctionType):
    print "Function"

# Now see if we can test subtypes
if issubclass(types.FunctionType, types.BuiltinFunctionType):
    print "Subclass"

# Now see if we can test subtypes
if issubclass(types.MethodType, types.FunctionType):
    print "Subclass"
