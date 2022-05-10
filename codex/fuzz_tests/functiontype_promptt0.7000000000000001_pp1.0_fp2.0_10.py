import types
# Test types.FunctionType
def a():
    return "hi"

# Test types.UnboundMethodType
class M:
    def b(self):
        return "hi"

# Test types.BuiltinFunctionType
def c():
    return "hi"

# Test types.BuiltinMethodType
class B:
    def d(self):
        return "hi"

# Test types.InstanceType
class I:
    __metaclass__ = type

    def e(self):
        return "hi"

# Test types.TypeType
class T:
    pass

# Test types.CodeType
def f():
    return "hi"

# Test types.ClassType
class C:
    pass

# Test types.MethodType
class Method:
    def g(self):
        return "hi"

# Test types.SliceType
sl = slice(0, 5, 2)

# Test types.TracebackType
import sys
ex = None
try:
    raise Exception("hi")
except:
    ex = sys.exc_info()[2]

