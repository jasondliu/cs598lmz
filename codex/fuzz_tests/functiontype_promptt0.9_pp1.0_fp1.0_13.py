import types
# Test types.FunctionType
f = types.FunctionType(source_code, globals())
ret = f()
assertEqual(ret, "Hello World!")
# Test types.FunctionType with closure
scope = {
    "i": 1
}
def f():
    i = i + 1
    return i
f = types.FunctionType(f.__code__, scope)
assertEqual(f(), 2)

# Test types.MethodType
c = MyClass()
assertEqual(types.MethodType(source_code, c)(), "Hello World!")

# Test types.BuiltinFunctionType
assertEqual(type(bin), types.BuiltinFunctionType)

# Test types.UnboundMethodType
assertEqual(type(MyClass.method), types.UnboundMethodType)

# Test types.TracebackType
import sys
def t(type, value, traceback): pass
assertIsInstance(sys.exc_info()[2], types.TracebackType) #@UndefinedVariable

# Test types.GetSetDescriptorType
def getx(self): pass
