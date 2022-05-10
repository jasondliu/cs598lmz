import types
# Test types.FunctionType
def f():
    pass
# Test types.MethodType
class C:
    def m(self):
        pass
# Test types.LambdaType
l = lambda: None

# Test types.GeneratorType
def g():
    yield 1

# Test types.CodeType
def f():
    pass

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]

# Test types.FrameType
def f():
    pass

# Test types.BuiltinFunctionType
import operator

# Test types.BuiltinMethodType
import operator

# Test types.ModuleType
import types

# Test types.DictProxyType
import types

# Test types.NotImplementedType
import types

# Test types.GetSetDescriptorType
import operator

# Test types.MemberDescriptorType
import operator

# Test types.WrapperDescriptorType
import operator

# Test types.XRangeType
import types

# Test types.EllipsisType

