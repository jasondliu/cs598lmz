import types
# Test types.FunctionType for a function object (built-in functions)
import __builtin__

def f(): pass
func = __builtin__.abs
print isinstance(func, types.FunctionType)

# Test types.FunctionType for a function object (defined functions)
print isinstance(f, types.FunctionType)

# Test types.LambdaType for a lambda object
print isinstance((lambda : 1), types.LambdaType)

# Test types.CodeType for a code object
print isinstance(f.func_code, types.CodeType)

def f(): pass

# Test types.GeneratorType for a generator function
print isinstance(f(), types.GeneratorType)

# Test types.MethodType for a method object
class C:
    def a(self): pass

print isinstance(C().a, types.MethodType)

print types.MethodType(f, None, C).im_class

# Test types.UnboundMethodType for an unbound method object
print type(f)
print isinstance(f, types.UnboundMethodType)


