import types
# Test types.FunctionType
try:
    types.FunctionType
except AttributeError:
    import sys
    print("SKIP")
    sys.exit()

def f(): pass

assert type(f) == types.FunctionType
assert type(f) != types.BuiltinFunctionType
assert type(abs) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
try:
    types.BuiltinMethodType
except AttributeError:
    import sys
    print("SKIP")
    sys.exit()

class C:
    def m(self): pass

assert type(C.m) == types.BuiltinMethodType
assert type(C().m) == types.BuiltinMethodType

# Test types.MethodType
try:
    types.MethodType
except AttributeError:
    import sys
    print("SKIP")
    sys.exit()

class C:
    def m(self): pass

assert type(C.m) == types.BuiltinMethodType
assert type(C().m) == types.BuiltinMethodType

# Test types.Frame
