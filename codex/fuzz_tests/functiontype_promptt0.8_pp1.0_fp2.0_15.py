import types
# Test types.FunctionType
try:
    # Test types.LambdaType
    a = lambda : 1
    # Test types.BuiltinFunctionType
    b = open
    # Test types.BuiltinMethodType
    c = list.pop
    # Test types.TypeType
    d = 1.
    # Test types.MethodType
    e = {}.has_key
except Exception, e:
    raise

# Test types.InstanceType
class A:
    def __init__(self):
        pass
a = A()

# Test types.ObjectType
# TODO: this doesn't work in ironpython as ObjectType does not exist
#try:
#    a = ObjectType
#except:
#    pass
# TODO: this doesn't work in ironpython as the class is not exposed directly
#try:
#    a = MethodWrapperType
#except:
#    pass

# Test types.StringTypes
# TODO: this doesn't work in ironpython as StringTypes does not exist
#try:
#    a = StringTypes
#except:
#    pass
