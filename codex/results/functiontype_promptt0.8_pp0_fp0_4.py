import types
# Test types.FunctionType, etc.

def f(): pass
def g(): pass
def h(): pass
def c(): pass
def d(): pass
def e(): pass

f.__class__ = types.BuiltinFunctionType
g.__class__ = types.MethodType
h.__class__ = types.ModuleType
c.__class__ = types.ClassType
d.__class__ = types.UnboundMethodType
e.__class__ = types.TypeType

if f.__class__ is not types.BuiltinFunctionType or \
   g.__class__ is not types.MethodType or \
   h.__class__ is not types.ModuleType or \
   c.__class__ is not types.ClassType or \
   d.__class__ is not types.UnboundMethodType or \
   e.__class__ is not types.TypeType:
    raise RuntimeError, 'Bad types.FunctionType, etc.'

def f(): pass
def g(): pass
def h(): pass
def c(): pass
def d(a): pass
def e(a,b): pass

if types
