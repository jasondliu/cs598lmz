import types
# Test types.FunctionType
def test_FunctionType_error():
    # Test to see if it fails when the wrong number of arguments are given.
    try:
        types.FunctionType()
    except:
        pass
    else:
        print 'types.FunctionType() did not raise an exception'

def test_FunctionType_pass():
    # Test to see if it passes when the correct number of arguments are given.
    try:
        types.FunctionType(lambda x: x, {})
    except:
        print 'types.FunctionType() raised an exception'

# Test types.BuiltinFunctionType
def test_BuiltinFunctionType_error():
    try:
        types.BuiltinFunctionType()
    except:
        pass
    else:
        print 'types.BuiltinFunctionType() did not raise an exception'

def test_BuiltinFunctionType_pass():
    try:
        types.BuiltinFunctionType(lambda x: x)
    except:
        print 'types.BuiltinFunctionType() raised an exception'

# Test types.MethodType
def test_MethodType_error():
