import types
types.CodeType = types.CodeType
types.FrameType = types.FrameType
types.FunctionType = types.FunctionType

types.MethodType = None
types.ClassType = None
types.BuiltinFunctionType = None
types.BuiltinMethodType = None

import sys as _sys

if _sys.version_info < (3, 7):
    types.TracebackType = types.TracebackType

if not hasattr(types, 'AsyncGeneratorType'):
    types.AsyncGeneratorType = None

if not hasattr(types, 'CoroutineType'):
    types.CoroutineType = None

if not hasattr(types, 'MappingProxyType'):
    types.MappingProxyType = None

if not hasattr(types, 'SimpleNamespace'):
    types.SimpleNamespace = None

if not hasattr(types, 'ChainMap'):
    types.ChainMap = None

if not hasattr(types, 'GeneratorType'):
    types.GeneratorType = None

