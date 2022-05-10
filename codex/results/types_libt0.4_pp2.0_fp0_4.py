import types
types.MethodType(func, None, None)

# Function type
types.FunctionType(func.__code__, func.__globals__, func.__name__, func.__defaults__, func.__closure__)

# Builtin function type
types.BuiltinFunctionType(abs)

# Builtin method type
types.BuiltinMethodType(list.append)

# Method wrapper type
types.MethodWrapperType(list.append)

# Wrapper descriptor type
types.WrapperDescriptorType(list.append)

# Class method type
types.ClassMethodType(list.append)

# Static method type
types.StaticMethodType(list.append)

# Code type
types.CodeType(func.__code__)

# Frame type
types.FrameType(None, "", "", "", "", "")

# Traceback type
types.TracebackType(None, None, None)

# Slice type
types.SliceType(None, None, None)

# Ellipsis type
types.EllipsisType
