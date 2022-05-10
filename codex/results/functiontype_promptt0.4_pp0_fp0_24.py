import types
# Test types.FunctionType
try:
    types.FunctionType
except AttributeError:
    pass
else:
    raise RuntimeError

class A:
    def f(self):
        print("A.f")

def f():
    print("f")

# Test types.BuiltinFunctionType
try:
    types.BuiltinFunctionType
except AttributeError:
    pass
else:
    raise RuntimeError

# Test types.MethodType
try:
    types.MethodType
except AttributeError:
    pass
else:
    raise RuntimeError

# Test types.BuiltinMethodType
try:
    types.BuiltinMethodType
except AttributeError:
    pass
else:
    raise RuntimeError

# Test types.ModuleType
try:
    types.ModuleType
except AttributeError:
    pass
else:
    raise RuntimeError

# Test types.LambdaType
try:
    types.LambdaType
except AttributeError:
    pass
else:
    raise RuntimeError

# Test types.GeneratorType
try:
    types.
