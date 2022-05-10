import types
# Test types.FunctionType
def func_returning_func():
    return lambda x: x

class A(object):
    def __init__(self):
        self.func = func_returning_func()

a = A()

print "Function type:", type(a.func) is types.FunctionType

# Test types.MethodType
class B(object):
    def __init__(self):
        self.func = func_returning_func()

    def method(self):
        return self.func

b = B()

print "Method type:", type(b.method()) is types.MethodType

# Test types.BuiltinFunctionType
print "Builtin function type:", type(abs) is types.BuiltinFunctionType

# Test types.BuiltinMethodType
print "Builtin method type:", type(list.append) is types.BuiltinMethodType

# Test types.InstanceType
print "Instance type:", type(A()) is types.InstanceType

# Test types.TracebackType
try:
    raise Exception
except Exception, e:
   
