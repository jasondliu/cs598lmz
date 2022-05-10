import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(int, types.FunctionType)
try:
    isinstance(None, types.FunctionType)
except TypeError:
    pass
else:
    raise Exception, "should have raised"
assert not isinstance(1, types.FunctionType)
def f(x): return x
try:
    isinstance(f, types.FunctionType)
except TypeError:
    pass
else:
    raise Exception, "should have raised"

# Test types.MethodType
def f(): pass
assert not isinstance(f, types.MethodType)
assert not isinstance(lambda: None, types.MethodType)
assert not isinstance(int, types.MethodType)
assert not isinstance(None, types.MethodType)
assert not isinstance(1, types.MethodType)
def f(x): return x
assert not isinstance(f, types.MethodType)

class C(object):
    def f(self): return 42
   
