import types
# Test types.FunctionType
def f():
    pass
try:
    x = types.FunctionType
except AttributeError:
    print "SKIP"
    raise SystemExit

class C: pass
print isinstance(f,types.FunctionType)
print isinstance(C,types.FunctionType)
