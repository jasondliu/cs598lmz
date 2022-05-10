import types
types.MethodType(lambda self : 42, 42)

# make sure we have the right type
import types
def f(): pass
f.__class__ is types.FunctionType

# make sure we have the right type
import types
def f(): pass
f.__class__ is types.BuiltinFunctionType

# make sure we have the right type
import types
def f(): pass
f.__class__ is types.MethodType

# make sure we have the right type
import types
def f(): pass
f.__class__ is types.BuiltinMethodType

# make sure we have the right type
import types
def f(): pass
f.__class__ is types.ModuleType

# make sure we have the right type
import types
def f(): pass
f.__class__ is types.FileType

# make sure we have the right type
import types
def f(): pass
f.__class__ is types.TracebackType

# make sure we have the right type
import types
def f(): pass
f.__class__ is types.FrameType

# make sure we have
