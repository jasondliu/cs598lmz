import types
# Test types.FunctionType and types.MethodType
try:
    ''.upper
    types.FunctionType
except:
    types.FunctionType = types.MethodType
    types.MethodType = types.BuiltinMethodType
try:
    types.BuiltinFunctionType
except:
    types.BuiltinFunctionType = types.BuiltinMethodType
    types.BuiltinMethodType = types.BuiltinFunctionType

try:
    types.UnboundMethodType
except:
    types.UnboundMethodType = types.MethodType

# Test how to get the name of a function
try:
    def foo(): pass
    foo.func_name
except:
    def nameof(obj):
        # This takes care of a difference between Jython and CPython.
        # In Jython function objects are methods and .__name__ gives the
        # name of the class method is bound to.
        if isinstance(obj, types.FunctionType):
            return obj.__name__
        else:
            return obj.__class__.__name__
else:
    def nameof(obj):
        return obj.
