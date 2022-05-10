import types
# Test types.FunctionType
def f(x):
    return x

def g():
    pass

class C:
    def m(self, x):
        return x

c = C()

# Functions
assert type(f) is types.FunctionType
assert type(g) is types.FunctionType
assert type(c.m) is types.MethodType
assert type(C.m) is types.FunctionType

assert type(f).__name__ == 'function'
assert type(g).__name__ == 'function'
assert type(c.m).__name__ == 'method'
assert type(C.m).__name__ == 'function'

# Built-in functions
import math
assert type(math.sin) is types.BuiltinFunctionType
assert type(math.sin).__name__ == 'builtin_function_or_method'

# Classes
assert type(C) is types.ClassType
assert type(C).__name__ == 'classobj'

# Instances
assert type(c) is types.InstanceType
assert type(c).__name__ == 'instance
