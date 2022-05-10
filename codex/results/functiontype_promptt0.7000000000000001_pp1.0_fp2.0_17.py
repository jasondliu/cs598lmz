import types
# Test types.FunctionType for function
# Test types.LambdaType for lambda
# Test types.BuiltinFunctionType for built-in functions
# Test types.MethodType for methods
# Test types.UnboundMethodType for unbound methods
# Test types.InstanceType for instances


# Test type of type(type)
type_of_type = type(type)
test.test_support.check_type_type(type_of_type, 'type', 'type')

# Test type of type(object)
type_of_object = type(object)
test.test_support.check_type_type(type_of_object, 'type', 'type')

# Test type of type(type) == type
if not type_of_type == type:
    raise test.test_support.TestFailed, 'type(type) == type'

# Test type of type(object) == type
if not type_of_object == type:
    raise test.test_support.TestFailed, 'type(object) == type'

# Test type of type(type(type)) == type
if not
