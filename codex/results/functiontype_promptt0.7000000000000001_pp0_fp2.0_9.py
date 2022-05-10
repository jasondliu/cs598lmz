import types
# Test types.FunctionType.__module__
def check(name):
    obj = eval(name)
    try:
        print getattr(obj, '__module__')
    except AttributeError:
        pass

check('types.FunctionType')
check('types.LambdaType')
check('types.GeneratorType')
check('types.ClassType')
check('types.InstanceType')
check('types.MethodType')
check('types.UnboundMethodType')
check('types.BuiltinFunctionType')
check('types.BuiltinMethodType')
check('types.ModuleType')
check('types.CodeType')
check('types.TracebackType')
check('types.FrameType')
check('types.BufferType')
check('types.DictProxyType')
check('types.NotImplementedType')
check('types.GetSetDescriptorType')
check('types.MemberDescriptorType')

# Test types.MemberDescriptorType.__module__
class X(object):
    def __get__(self, obj, type):
        pass
    def __set
