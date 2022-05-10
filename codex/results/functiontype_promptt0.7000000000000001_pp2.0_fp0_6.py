import types
# Test types.FunctionType
def a(x=3):
    pass
#assert type(a)==types.FunctionType
# Test types.BuiltinFunctionType
#assert type(abs)==types.BuiltinFunctionType
# Test types.ClassType
#assert type(type)==types.ClassType
# Test types.UnboundMethodType
#assert type(type.__new__)==types.UnboundMethodType
# Test types.InstanceType
#assert type(a)==types.InstanceType
# Test types.MethodType
#assert type(a.__doc__)==types.MethodType
# Test types.BuiltinMethodType
#assert type(type.__doc__)==types.BuiltinMethodType
class X(object):
    def __init__(self):
        pass
# Test types.LambdaType
#assert type((lambda x:x*x))==types.LambdaType
# Test types.GeneratorType
#assert type((x for x in range(10)))==types.GeneratorType
# Test types.TracebackType
#assert type(sys.exc_info()[
