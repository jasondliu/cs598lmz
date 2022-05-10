import types
# Test types.FunctionType

def f(x):
    return x

print type(f)
print type(f(1))

class C(object):
    def g(self):
        return 2

print type(C.g)
print type(C.g(C))

# Test types.BuiltinFunctionType

def is_builtin(x):
    if type(x) != types.BuiltinFunctionType:
        raise Exception, "Not builtin"

is_builtin(abs)
is_builtin(f)

# Test types.MethodType

def is_method(x):
    if type(x) != types.MethodType:
        raise Exception, "Not method"

is_method(C.g)
is_method(C().g)

# Test types.ClassType

def is_class(x):
    if type(x) != types.ClassType:
        raise Exception, "Not class"

is_class(C)

# Test types.InstanceType

def is_instance(x):
    if type(x) !=
