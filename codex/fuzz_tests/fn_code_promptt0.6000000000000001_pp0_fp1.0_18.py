fn = lambda: None
# Test fn.__code__ to see if it's an instance of the types we want to check for.
# The __code__ object is a read-only attribute.
fn.__code__ = types.CodeType
fn.__code__ = types.FrameType
fn.__code__ = types.FunctionType
fn.__code__ = types.GeneratorType
fn.__code__ = types.GetSetDescriptorType
fn.__code__ = types.LambdaType
fn.__code__ = types.MappingProxyType
fn.__code__ = types.MemberDescriptorType
fn.__code__ = types.MethodType
fn.__code__ = types.ModuleType
fn.__code__ = types.SimpleNamespace
fn.__code__ = types.TracebackType

# Test fn.__globals__ to see if it's an instance of the types we want to check for.
# The __globals__ object is a read-only attribute.
fn.__globals__ = types.CodeType
fn.__globals__ = types.FrameType
fn.__globals__ =
