import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType
# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
# Test types.LambdaType
f = lambda x:x
assert type(f) == types.LambdaType
# Test types.GeneratorType
def f(): yield 1
assert type(f()) == types.GeneratorType
# Test types.CodeType
def f(): pass
assert type(f.__code__) == types.CodeType
# Test types.FrameType
assert type(sys._getframe()) == types.FrameType
# Test types.TracebackType
try:
    raise Exception
except Exception:
    tb = sys.exc_info()[2]
assert type(tb) == types.TracebackType
# Test types.GetSetDescriptorType
class C(object):
    def fset(self, x):
        self.x = x
    def fget(self):
        return self.x
    prop = property(fget, fset)
c = C()

